import os
import csv

# 현재 작업 디렉토리 출력
current_path = os.getcwd()
print(f"현재 작업 디렉토리: {current_path}")

# 텍스트 파일을 읽어들임
target_filename = 'Test07_MeshData'

input_filename = './txt-to-csv/' + target_filename + '.txt'
output_filename = './txt-to-csv/' + target_filename + '.csv'

# 파일을 읽어옴
with open(input_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# CSV 파일에 저장할 데이터 리스트
csv_data = []

# 현재 오브젝트의 데이터를 저장할 임시 딕셔너리
current_object = {}

# 각 줄을 순회하며 데이터 파싱
for line in lines:
    line = line.strip()  # 줄 끝의 공백 제거
    if line.startswith("Object Name:"):
        # 새로운 오브젝트 데이터 시작 시 기존 데이터 저장
        if current_object:
            csv_data.append(current_object)
        # 오브젝트 이름 초기화
        current_object = {'Object Name': line.split(": ", 1)[1]}  # 첫 번째 콜론 이후의 내용만 가져옴
    elif line.startswith("Vertex Count:"):
        current_object['Vertex Count'] = int(line.split(": ", 1)[1])
    elif line.startswith("Triangle Count:"):
        current_object['Triangle Count'] = int(line.split(": ", 1)[1])
    elif line.startswith("Bounds Size:"):
        bounds = line.split(": ", 1)[1].strip("()").split(", ")
        current_object['Bounds Size X'] = float(bounds[0])
        current_object['Bounds Size Y'] = float(bounds[1])
        current_object['Bounds Size Z'] = float(bounds[2])

# 마지막 오브젝트 데이터 추가
if current_object:
    csv_data.append(current_object)

# CSV 파일로 저장
with open(output_filename, 'w', newline='') as csvfile:
    fieldnames = ['Object Name', 'Vertex Count', 'Triangle Count', 'Bounds Size X', 'Bounds Size Y', 'Bounds Size Z']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for obj in csv_data:
        writer.writerow(obj)

print(f"CSV 파일 '{output_filename}'이(가) 성공적으로 생성되었습니다.")