n1, n2, n3, n4 = list(map(float, input().split()))
avg = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print(f"Media: {avg:.1f}")
if avg >= 7.0:
    print("Aluno aprovado.")
if avg < 5.0:
    print("Aluno reprovado.")

if avg >= 5.0 and avg <= 6.9:
    print("Aluno em exame.")
    examScore = float(input())
    print(f"Nota do exame: {examScore:.1f}")
    finalAvg = (examScore + avg) / 2
    if finalAvg >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {finalAvg:.1f}")