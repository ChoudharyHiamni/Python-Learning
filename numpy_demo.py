
import numpy as np
                        #1D ARRAY,INDEXING AND SLICING

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))

# print(np.__version__)

# print(arr[0])
# print(arr[2:4])
# print(arr[2] + arr[3])

                     #2S ARRAY,INDEXING AND SLICING

# arr2=np.array([[1,2,3,4],[6,7,8,9]])
# print(arr2)
# print(arr2[0,2])
# print(arr2[1,3])
# print(arr2[1,-1])


# arr3=np.array([1,2,3,4,5,6,7,8,9])
# print(arr3[-3:-1])
# # print(arr3[1:5:2]) 
# print(arr3[::2])  #include all elements with step size 2
# print(arr3[::-1])  #reverse the array

                         #NUMPY COPY AND VIEW
#copy() in NumPy creates an independent array, so modifying the original array does not affect the copied array.

# arr=np.array([1,2,3,4,5])
# x=arr.copy()  #creates a new array,independent of the original array
# arr[0]=10
# print(arr)
# print(x)


#view() creates a new array object that shares memory with the original array, so changes in one affect the other.
# arr=np.array([1,2,3,4,5])
# x=arr.view()  
# arr[0]=10
# print(arr)
# print(x)


                            #NUMPY ARRAY SAHPE
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)  #OUTPUT:(2,4) 2 ROWS AND 4 COLUMNS AS THERE ARE 2 ROWS AND 4 ELEMENT IN EACH ROW



# arr = np.array([1, 2, 3, 4], ndmin=5)  #NDIMN SPECIFY NUMBER OF DIMENSIONS AND CREATE ARRAY ACCORDING TO THAT 
# print(arr)
# print('shape of array :', arr.shape)  #OUTPUT:(1, 1, 1, 1, 4) 5 DIMENSIONS WITH 4 ELEMENTS IN THE LAST DIMENSION

                             #RESHAPING NUMPY ARRAY
# arr=np.array([1,2,3,4,5,6,7,8])
# newarr=arr.reshape(2,4)  #RESHAPE 1D ARRAY TO 2D ARRAY WITH 2 ROWS AND 4 COLUMNS
# print(newarr)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)  #RESHAPE 1D ARRAY TO 3D ARRAY WITH 2 BLOCKS,3 ROWS AND 2 COLUMNS  
# print(newarr)
#newarr = arr.reshape(2, 3, 2)  #RESHAPE 1D ARRAY TO 3D ARRAY WITH 2 BLOCKS,3 ROWS AND 2 COLUMNS 

  

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)  #RESHAPE 2D ARRAY TO 1D ARRAY USING -1

# print(newarr)

    
                   #NUMPY ITERATING ARRAYS
# arr=np.array([1,2,3,4,5])
# for x in arr:
#     print(x)

# arr1=np.array([[1,2,3,4],[5,6,7,8]])
# for y in arr1:
#     print(y)

 
                           #Iterate on each scalar element of the 2-D array
# arr2=np.array([[1,2,3,4],[5,6,7,8]])
# for x in arr2:
#     for y in x:
#         print(y)



                #ITERATE DOWN TO THE SCALARS
# arr=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

   
                      #NUMPY ARRAY JOIN
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# arr3=np.concatenate((arr1,arr2))
# print(arr3)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))

# print(arr)


             #JOIN 2D ARRAY
# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)

# print(arr)

                       #JOINING ARRAY USING STACK FUNCTION

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

                         #STACKING ALONG ROWS
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)


                        #STACKING ALONG COLUMN
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))

# print(arr)

               #STACKING ALONG HEIGHT


# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.dstack((arr1, arr2))

# print(arr)

               #NUMPY ARRAY SPLIT

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)



# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 4)

# print(newarr)

                                #NP ARRAY SEARCH
# arr=np.array([1,2,3,4,5])
# x=np.where(arr==4)
# print(x)

# y=np.where(arr%2==0)
# print(y)

                               #SEARCH SORTED
# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 7)

# print(x)

                                #NUMPY ARRAY SORT

# arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))


# arr = np.array([True, False, True])

# print(np.sort(arr))


                       #SORTED 2D ARRAY
# arr = np.array([True, False, True])

# print(np.sort(arr))


# arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))


                            #NUMPY ARRAY FILTER
# Getting some elements out of an existing array and creating a new array out of them is called filtering.  

# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]  

# newarr = arr[x]

# print(newarr)  


          #Create a filter array that will return only even elements from the original array:
# arr=np.array([1,2,3,4,5,6,7])
# filter_arr=arr%2==0
# new_arr=arr[filter_arr]
# print(new_arr)


               #Create a filter array that will return only values higher than 42
# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

