# Academic-Year
This Python program predicts progression outcomes at the end of each academic year based on the University's regulations. The predictions are made using the data provided in Table 1, which defines the progression outcomes for different volumes of credit at each level. The program helps identify whether a student will progress, not progress (module retriever), or be excluded based on their credit volume.
 

 
 Pass   Defer   Fail      Result
 
 120    0       0        Progress
 100    20      0        Progress (module trailer) 
 100    0       20       Progress (module trailer)
 80     40      0        Do not Progress – module retriever
 80     20      20       Do not Progress – module retriever 
 80     0       40       Do not Progress – module retriever
 60     60      0        Do not progress – module retriever 
 60     40      20       Do not progress – module retriever 
 60     20      40       Do not progress – module retriever 
 60     0       60       Do not progress – module retriever 
 40     80      0        Do not progress – module retriever 
 40     60      20       Do not progress – module retriever 
 40     40      40       Do not progress – module retriever 
 40     20      60       Do not progress – module retriever 
 40     0       80       Exclude 
 20     100     0        Do not progress – module retriever
 20     80      20       Do not progress – module retriever 
 20     60      40       Do not progress – module retriever 
 20     40      60       Do not progress – module retriever 
 20     20      80       Exclude 
 20     0       100      Exclude 
 0      120     0        Do not progress – module retriever 
 0      100     20       Do not progress – module retriever 
 0      80      40       Do not progress – module retriever 
 0      60      60       Do not progress – module retriever 
 0      40      80       Exclude 
 0      20      100      Exclude
 0      0       120      Exclude 
 
