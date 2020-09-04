class My_resume :

    def __init__ (self) :
        self._let_me = ""
        self._introduce  = ""
        self._myself = ""
        self._and_job_experience= ""
        self._sincerely = ""
    
    def let_me (self) :
        self._let_me  = "First,I really appreciate you for executing this program,this really meaning to me."
        return self 
    
    def introduce(self) :
        self._introduce = "I hold a bachelor degree with a major in Finance. "
        return self

    def my_self (self) :
        self._my_self = "many license related to bank ,and get the graduation standard of the Department of English Language."
        return self

    def and_job_experience(self) :
        self._and_job_experience = "I used to been a Real estate broker,and last job position is assistant relationship manager of bank."
        return self

    def sincerely (self) :
        self._sincerely = "Now I found that I am more enthusiastic about writing programs,which can make our lives more convenient and achieve more interesting ideas in life"
        return self
        


    def __str__ (self) :
        return ("Dear HR : \n"  "{0}\n\rMy name is Ming Ting Tsai , I`m graduate from Providence University.{1}"
         "\n\rBesides my major,I have also taken{2}""\n\rAfter graduating from school ,{3}"
         "\n\rThe main work content is enterprise loans,This gave me a lot of valuable experience and let me understand the various loan businesses of banks.\n\r""{4},"
         "\n\rso this motivates me to be a software engineer,and trust me I will not let you down,and thank you for reading my resume.\n\nSincerely\n\nMing Ting Tsai").format(self._let_me ,
                                                                                                                                                                               self._introduce,
                                                                                                                                                                               self._my_self ,
                                                                                                                                                                               self._and_job_experience,
                                                                                                                                                                               self._sincerely)



if __name__ == "__main__" :
    For_dear_HR = My_resume()

    print(For_dear_HR.let_me().introduce().my_self().and_job_experience().sincerely())
    
