def same_in_reverse(str):
    l1 = list(str)
    l2 = l1.copy()
    l2.reverse()
    
    if l1 == l2:
        return True
    return False

print(same_in_reverse("dad"))