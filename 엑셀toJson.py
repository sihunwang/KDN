#엑셀 파일을 json으로 바꾸는 코드

import pandas as pd
import json

# 1. 엑셀 파일 경로
excel_path = "소재지좌표.xlsx"  # 같은 폴더 안에 있어야 함

# 2. 엑셀 불러오기
df = pd.read_excel(excel_path)

# 3. 좌표 파싱 함수
def parse_coords(coord_str):
    try:
        # "(lat, lng)(lat, lng)..."
        coord_str = coord_str.strip()
        if coord_str.startswith("("): coord_str = coord_str[1:]
        if coord_str.endswith(")"): coord_str = coord_str[:-1]
        pairs = coord_str.split(")(")
        return [list(map(float, pair.split(','))) for pair in pairs]
    except:
        return []

# 4. 변환 결과 리스트 생성
results = []

for _, row in df.iterrows():
    id_str = str(row[0]).strip()
    region = str(row[1]).strip()
    coord_string = str(row[2]).strip()
    coords = parse_coords(coord_string)

    if len(coords) >= 3:
        color = "#8B4513" if id_str.startswith("1") else "#800080"  # 갈색 or 보라색
        results.append({
            "id": id_str,
            "region": region,
            "coords": coords,   # [[lat, lng], ...]
            "color": color
        })

# 5. JSON 파일로 저장
with open("parcel_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ 필지 {len(results)}개가 parcel_data.json에 저장되었습니다.")
