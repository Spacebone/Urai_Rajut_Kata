def urai(kata):
    hasil = ''
    for i in range(len(kata)):
        for j in range(i):
            hasil = hasil + kata[j]
        hasil = hasil + kata[i]
    return hasil

# def rajut(kata):
#     hasil = ''
#     for i in range(len(kata)):
#         for j in range(i):
#             hasil = kata.append[i]
#             i += 1
#     return hasil

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))