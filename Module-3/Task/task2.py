class studinfo:
    stid=101
    stname="prit"

    def ID(self):
        print("this is ID using in function...")

    def Name(self):
        print("this is name using in function...")

st=studinfo()
print(st.stid)
print(st.stname)
st.ID()
st.Name()