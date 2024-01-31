class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q 
        self.e = e
        self.n = self.p * self.q
        self.phi_n = (self.p-1)*(self.q-1)
        self.d = pow(e,-1,self.phi_n)
        pass
    
    def encrypt(self, m):
        return pow(m,self.e,self.n)
    
    def decrypt(self, c):
        return pow(c,self.d,self.n)
