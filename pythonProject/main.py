## 조건문 연습문제 (1)
## 2019312492 이다은


rate = input("회원 등급을 입력하세요 : ")
price = int(input("제품의 가격을 입력하세요 : "))

print("제품의 가격은 ", end="")
if rate == "Diamond":
    print("{0:.1f}원입니다. 할인율 : Diamond = 0.4".format(price * 0.6))
elif rate == "Gold":
    print("{0:.1f}원입니다. 할인율 : Gold = 0.3".format(price * 0.7))
elif rate == "Silver":
    print("{0:.1f}원입니다. 할인율 : Silver = 0.2".format(price * 0.8))
elif rate == "Bronze":
    print("{0:.1f}원입니다. 할인율 : Bronze = 0.1".format(price * 0.9))
else:
    print("올바르지 않은 등급입니다.")


