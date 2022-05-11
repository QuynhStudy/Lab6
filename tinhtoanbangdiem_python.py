class BANGDIEM():
    def load_dulieu(self):
        self.file_dct=input('Enter file: ')
        if len(self.file_dct)<1:
            self.file_dct='C:\\Users\\Python\\diem_chitiet.txt'
        return self.file_dct
    def dl_so(self):
        self.line=self.line.rstrip().split()
        self.line=''.join(self.line)
        self.line=self.line.split(';')
        for i in range(1,len(self.line)):
            self.line[i]=float(self.line[i])
        return self.line
    def tinhdiem_trungbinh(self,file_dct):
        self.file_dct=file_dct
        self.f=open(file_dct)
        self.mon_hoc=['Toan','Ly','Hoa','Sinh','Van','Anh','Su','Dia']
        self.dict={}
        for self.line in self.f:
            if self.line.startswith('Ma HS'):
                continue
            self.line=self.line.rstrip().split()
            self.line=''.join(self.line)
            self.line=self.line.split(';')
            self.diemtrungbinh={}
            for self.lst in self.line:
                if self.lst in self.line[1:5]:
                    self.y=self.lst.split(',')
                    self.dtb=round((float(self.y[0])*5+float(self.y[1])*10+float(self.y[2])*15+float(self.y[3])*70)/100,2)
                    self.diemtrungbinh.setdefault(self.mon_hoc[self.line.index(self.lst)-1],self.dtb)
                elif self.lst in self.line[5:]:
                    self.y=self.lst.split(',')
                    self.dtb=round((float(self.y[0])*5+float(self.y[1])*10+float(self.y[2])*10+float(self.y[3])*15+float(self.y[4])*60)/100,2)
                    self.diemtrungbinh.setdefault(self.mon_hoc[self.line.index(self.lst)-1],self.dtb)
            self.dict.setdefault(self.line[0],self.diemtrungbinh)
        self.f.close()
        return self.dict
    def luudiem_trungbinh(self,file_dct,dtb,file_dtb):
        self.file_dct=file_dct
        self.dtb=dtb
        self.f=open(file_dct)
        self.file_dtb=file_dtb
        with open(self.file_dtb,'w') as self.nf:
            self.nf.write(self.f.readlines()[0])
            for self.key in self.dtb:
                self.nf.write(str(self.key)+';'+str(self.dtb[self.key]['Toan'])+';'+str(self.dtb[self.key]['Ly'])+';'+str(self.dtb[self.key]['Hoa'])+';'+str(self.dtb[self.key]['Sinh'])+';'+str(self.dtb[self.key]['Van'])+';'+str(self.dtb[self.key]['Anh'])+';'+str(self.dtb[self.key]['Su'])+';'+str(self.dtb[self.key]['Dia'])+'\n')
        self.f.close()
        return self.file_dtb

class DANHGIA(BANGDIEM):
    def xeploai_hocsinh(self,file_dct,file_dtb):
        self.file_dtb=file_dtb
        with open(file_dtb) as self.file:
            self.xl_hs={}
            for self.line in self.file:
                if self.line.startswith('Ma HS'):
                    continue
                self.line=super().dl_so()
                self.dtbm=min(self.line[1:len(self.line)])
                if (((self.line[1]+self.line[5]+self.line[6])*2.0+(self.line[2]+self.line[3]+self.line[4]+self.line[7]+self.line[8])*1.0)/11.0)>9.0 and self.dtbm>=8.0:
                    self.xl_hs[self.line[0]]=self.xl_hs.get(self.line[0],'Xuat sac')
                elif (((self.line[1]+self.line[5]+self.line[6])*2.0+(self.line[2]+self.line[3]+self.line[4]+self.line[7]+self.line[8])*1.0)/11.0)>8.0 and self.dtbm>=6.5:
                    self.xl_hs[self.line[0]]=self.xl_hs.get(self.line[0],'Gioi')
                elif (((self.line[1]+self.line[5]+self.line[6])*2.0+(self.line[2]+self.line[3]+self.line[4]+self.line[7]+self.line[8])*1.0)/11.0)>6.5 and self.dtbm>=5.0:
                    self.xl_hs[self.line[0]]=self.xl_hs.get(self.line[0],'Kha')
                elif (((self.line[1]+self.line[5]+self.line[6])*2.0+(self.line[2]+self.line[3]+self.line[4]+self.line[7]+self.line[8])*1.0)/11.0)>6.0 and self.dtbm>=4.5:
                    self.xl_hs[self.line[0]]=self.xl_hs.get(self.line[0],'TB kha')
                else:
                    self.xl_hs[self.line[0]]=self.xl_hs.get(self.line[0],'TB')
            return self.xl_hs
        self.file.close()
    def xeploai_thidaihoc_hocsinh(self,file_dtb):
        self.file_dtb=file_dtb
        with open(file_dtb) as self.file:
            self.xl_tdh={}
            for self.line in self.file:
                if self.line.startswith('Ma HS'):
                    continue
                self.line=super().dl_so()
                A=[self.line[1],self.line[2],self.line[3]]
                A1=[self.line[1],self.line[2],self.line[6]]
                B=[self.line[1],self.line[3],self.line[4]]
                C=[self.line[5],self.line[7],self.line[8]]
                D=[self.line[1],self.line[5],self.line[6]]
                def xeploai(khoi):
                    if khoi in [A,A1,B]:
                        if sum(khoi)>=24:
                            return 1
                        elif 18<=sum(khoi)<24:
                            return 2
                        elif 12<=sum(khoi)<18:
                            return 3
                        else:
                            return 4
                    if khoi==C:
                        if sum(khoi)>=21:
                            return 1
                        elif 15<=sum(khoi)<21:
                            return 2
                        elif 12<=sum(khoi)<15:
                            return 3
                        else:
                            return 4
                    if khoi==D:
                        if (sum(khoi)+khoi[2])>=32:
                            return 1
                        elif 24<=(sum(khoi)+khoi[2])<32:
                            return 2
                        elif 20<=(sum(khoi)+khoi[2])<24:
                            return 3
                        else:
                            return 4
                self.kq_xeploai=[xeploai(A),xeploai(A1),xeploai(B),xeploai(C),xeploai(D)]
                self.xl_tdh[self.line[0]]=self.xl_tdh.get(self.line[0],self.kq_xeploai)
        self.file.close()
        return self.xl_tdh
def main():
    f=DANHGIA()
    file_dct=f.load_dulieu()
    file_dtb='C:\\Users\\Python\\diem_trungbinh.txt'
    dtb=f.tinhdiem_trungbinh(file_dct)
    file_dtb=f.luudiem_trungbinh(file_dct,dtb,file_dtb)
    with open('C:\\Users\\Python\\danhgia_hocsinh.txt','w') as file:
        file.write('Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n')
        xl=f.xeploai_hocsinh(file_dct,file_dtb)
        xl_dh=f.xeploai_thidaihoc_hocsinh(file_dtb)
        for key in xl:
            file.write(str(key)+';'+str(xl[key])+';'+str(xl_dh[key][0])+";"+str(xl_dh[key][1])+';'+str(xl_dh[key][2])+';'+str(xl_dh[key][3])+';'+str(xl_dh[key][4])+'\n')
    file.close()

main()

class TUNHIEN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,file_dtb):
        self.file_dtb=file_dtb
        with open(file_dtb) as self.file:
            self.xl_tdh={}
            for self.line in self.file:
                if self.line.startswith('Ma HS'):
                    continue
                self.line=super().dl_so()
                A=[self.line[1],self.line[2],self.line[3]]
                A1=[self.line[1],self.line[2],self.line[6]]
                B=[self.line[1],self.line[3],self.line[4]]
                def xeploai(khoi):
                    if khoi in [A,A1,B]:
                        if sum(khoi)>=24:
                            return 1
                        elif 18<=sum(khoi)<24:
                            return 2
                        elif 12<=sum(khoi)<18:
                            return 3
                        else:
                            return 4
                self.kq_xeploai=[xeploai(A),xeploai(A1),xeploai(B)]
                self.xl_tdh[self.line[0]]=self.xl_tdh.get(self.line[0],self.kq_xeploai)
        self.file.close()
        return self.xl_tdh
class XAHOI(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,file_dtb):
        self.file_dtb=file_dtb
        with open(file_dtb) as self.file:
            self.xl_tdh={}
            for self.line in self.file:
                if self.line.startswith('Ma HS'):
                    continue
                self.line=super().dl_so()
                C=[self.line[5],self.line[7],self.line[8]]
                def xeploai(khoi):
                    if khoi==C:
                        if sum(khoi)>=21:
                            return 1
                        elif 15<=sum(khoi)<21:
                            return 2
                        elif 12<=sum(khoi)<15:
                            return 3
                        else:
                            return 4
                self.kq_xeploai=[xeploai(C)]
                self.xl_tdh[self.line[0]]=self.xl_tdh.get(self.line[0],self.kq_xeploai)
        self.file.close()
        return self.xl_tdh
class COBAN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,file_dtb):
        self.file_dtb=file_dtb
        with open(file_dtb) as self.file:
            self.xl_tdh={}
            for self.line in self.file:
                if self.line.startswith('Ma HS'):
                    continue
                self.line=super().dl_so()
                D=[self.line[1],self.line[5],self.line[6]]
                def xeploai(khoi):
                    if khoi==D:
                        if (sum(khoi)+khoi[2])>=32:
                            return 1
                        elif 24<=(sum(khoi)+khoi[2])<32:
                            return 2
                        elif 20<=(sum(khoi)+khoi[2])<24:
                            return 3
                        else:
                            return 4
                self.kq_xeploai=[xeploai(D)]
                self.xl_tdh[self.line[0]]=self.xl_tdh.get(self.line[0],self.kq_xeploai)
        self.file.close()
        return self.xl_tdh
