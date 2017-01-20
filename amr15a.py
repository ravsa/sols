L = int(raw_input())
soldiers = map(lambda x: 1 if int(x) & 1 == 0 else 0,
               raw_input().split())
even = soldiers.count(1)
odd = L - even
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
