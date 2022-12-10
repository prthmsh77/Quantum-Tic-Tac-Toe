import numpy as np
from superposition import quantum_superposition
import streamlit as st
 

def random_value():
    res  = quantum_superposition()
    values = list(res.values())
    keys = list(res.keys())
    random_value = '|' + str(keys[np.argmax(values)])+ '>'
    return random_value

def validate(arr):
    flag= True
    zero_ket = "|0>"
    one_ket  = "|1>"

    if arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success('computer wins') 
        flag = False

    elif arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success('User wins') 
        flag = False

    elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,0]==zero_ket:
        st.success('computer wins') 
        flag = False

    elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success('User wins') 
        flag = False

    # elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
    #     st.success('User wins') 
    #     flag = False

    # elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
    #     st.success('computer wins') 
    #     flag = False

    if not flag:
        return 0    

    if flag:
        for index in [0,1,2]:
            if(list(arr[index])==[one_ket,one_ket,one_ket]):
                st.success('user win')
                return 0

        for index in [0,1,2]:
            if(list(arr[index])==[zero_ket,zero_ket,zero_ket]):
                st.success('compuetr win')
                return 0
        
        for index in [0,1,2]:
            if(list(arr[:,index])==[one_ket,one_ket,one_ket]):
                st.success('user win')
                return 0

        for index in [0,1,2]:
            if(list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
                st.success('compuetr win')
                return 0
        if '|ψ>' not in arr:
            st.write("its a draw")
            return 0
    return 1

