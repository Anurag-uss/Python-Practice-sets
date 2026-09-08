marks={
    "Anurag" : 500,
    "Shubham" : 400,
    "Aditya"  : 300,
}

#items    (will give the items of dictionary in form of tuples)
print(marks.itmes())


#keys     (will give the values of the left hand side items eg. "Anurag".....)
print(marks.keys())       


#values   (will give the values of the right and side items eg. 500.....)
print(marks.values())


#update method        (will update the value because its mutable)
marks.update({"Anurag": 600})         
marks.update({"Riya": 200})      #values which are not present will be added


#get method           (will return the value of the required item if not then retn (none))
print(marks.get("Anurag"))
print(marks["Anurag"])

#difference: 
print(marks.get("Anurag2"))      #will return none
print(marks["Anurag2"])          #will return error

