import pandas as pd
import streamlit as st 
import numpy as np
from game import  random_value,validate
from superposition import quantum_superposition
import math
from matplotlib import pyplot as plt
from entgld import entangled,img
from qiskit.visualization import plot_bloch_vector
from data import superposition_info,entanglment_info,instruction_info

def main():
    st.title("QUANTUM COMPUTING")
    
    menu=["Play","Instructions","Superposition","Enganglement","About"]
    option = st.sidebar.selectbox("menu",menu,)

    if option =="Play":
        st.header("Quantum tic tac toe")
        st.subheader("Quantum play begins")
        st.write("computer => |0>")
        st.write("user => |1>")
        psi="|ψ>"
        if 'board' not in st.session_state:
            st.session_state.board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves = [0,1,2,3,4,5,6,7,8,9]
        moves = st.selectbox("make a move",st.session_state.available_moves)

        if moves ==1:
            if st.session_state.board[0,0]==psi:
                st.session_state.board[0,0]=random_value()
                user_flag = validate(st.session_state.board)
                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
               st.dataframe(st.session_state.board)

        elif moves ==2:
            if st.session_state.board[0,1]==psi:
                st.session_state.board[0,1]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)
    
        elif moves ==3:
            if st.session_state.board[0,2]==psi:
                st.session_state.board[0,2]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)
    
        elif moves ==4:
            if st.session_state.board[1,0]==psi:
                st.session_state.board[1,0]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
               st.dataframe(st.session_state.board)
    
        elif moves ==5:
            if st.session_state.board[1,1]==psi:
                st.session_state.board[1,1]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)

        elif moves ==6:
            if st.session_state.board[1,2]==psi:
                st.session_state.board[1,2]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)

            else:
              st.dataframe(st.session_state.board)
    
        
        elif moves ==7:
            if st.session_state.board[2,0]==psi:
                st.session_state.board[2,0]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)
    
        elif moves ==8:
            if st.session_state.board[2,1]==psi:
                st.session_state.board[2,1]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                    
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)
    
        elif moves ==9:
            if st.session_state.board[2,2]==psi:
                st.session_state.board[2,2]=random_value()
                user_flag = validate( st.session_state.board)
                if not user_flag:
                    st.dataframe( st.session_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col =(comp_square-1)%3
                row =math.floor((comp_square-1)/3)
                comp_value = random_value()
                if st.session_state.board[row,col]==psi :
                    st.session_state.board[row,col] = comp_value
                comp_flag = validate( st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computers move: ",comp_square)
                st.write("compuetrs value: ",comp_value)
                st.dataframe(st.session_state.board)
            else:
              st.dataframe(st.session_state.board)
        else:
            st.dataframe(st.session_state.board)
   
    elif option=="Superposition":
        st.subheader("Superposition")
        st.write(superposition_info())
        res  = quantum_superposition()
        values = list(res.values())
        keys = list(res.keys())
        fig = plt.figure()
        plt.xlabel("probability of qubit in superposition")
        plt.ylabel("no of cases")
        plt.bar(keys,values)
        st.write(fig)
        if st.button("measure qubit"):
            random = str(keys[np.argmax(values)])
            st.write("qubit collapsed to "+"|"+ random +">" )
            if random == "1":
                 img1 = plot_bloch_vector([0,0,-1], title="Bloch Sphere showing superposition after measurement")
                 fig1 = plt.figure(img1)
                 st.write(fig1)
                 return 0
                 
            else:
                 img1 = plot_bloch_vector([0,0,1], title="Bloch Sphere showing superposition after measurement")
                 fig1 = plt.figure(img1)
                 st.write(fig1)
                 return 0

        else:
            img1 = plot_bloch_vector([0,1,0], title="Bloch Sphere showing superposition before measurement")
            fig1 = plt.figure(img1)
            st.write(fig1)

    elif option=="Enganglement":
        st.subheader("Enganglement")
        st.write(entanglment_info())
        res  = entangled()
        values = list(res.values())
        keys = list(res.keys())
        fig = plt.figure()
        plt.xlabel("probability of entagled qubits")
        plt.ylabel("no of cases")
        plt.bar(keys,values)
        st.write(fig)
        fig1 = plt.figure(img())
        st.write(fig1)
        
   

    elif option == "Instructions":
        st.subheader("instructions") 
        psi="|ψ>"
        board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
        st.write(instruction_info())
        st.write("board:")
        st.dataframe(board)
        board_numbering = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
        st.write("|0> is the symbol chosen by the computer")
        st.write("|1> is the symbol chosen by the user")
        st.write("Both the user and the computer play turn by turn and choose the particular box to play their move.")
        st.dataframe(board_numbering)
    else:
        st.header("About")
        st.subheader("Refrence:")
        st.write("""1)Python documentation\n
2)Qiskit documentation\n
3)Streamlit documentation\n""")
        st.subheader("Guided by AMIT UPHAD sir")

    


if __name__ == '__main__':
    condition = main()
    if condition ==0:
        st.subheader("Game over")
        


