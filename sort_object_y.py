obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'pen': [155, 100], 'mouse':
[200, 45], 'remote': [298, 165], 'fan': [300, 36]}

Sorted_obj  = sorted(obj_detected.items(), key=lambda x:x[1][1])
print(Sorted_obj)