def getGrade(grade):
    # grade=grade*10
    if grade<=4.0 and grade>=3.6:
        return("A")
    if grade<=3.6 and grade>=3.4:
        return("B")
    if grade<=3.4 and grade>=3.2:
        return("C")
    elif grade<0.0:
        return("Negative Grade not Possible")
    else:
        return("Fail")
def main():
    # print("Hello from datascience!")
    grade=float(input("Enter Grade:"))
    print(getGrade(grade))

if __name__ == "__main__":
    main()
