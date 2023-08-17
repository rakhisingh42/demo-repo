#Write a program for rearrange the sequence of elements based on length of character in value
def rearr_seq(seq) :
    return sorted(seq, key=len)

seq = ["Add", "Bold", "Queen", "Rakhi","ShivaniSurolia", "TinaSaluja"]
rearrange_seq = rearr_seq(seq)
print(rearrange_seq)