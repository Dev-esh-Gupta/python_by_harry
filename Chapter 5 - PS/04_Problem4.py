st = set()

st.add(18)
st.add('18')
st.add(18.0)

# 18.0 and 18 will be treated as same

print(len(st), st)