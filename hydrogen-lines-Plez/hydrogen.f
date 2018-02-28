        parameter (nn=2000)
        dimension alam(nn),nlow(nn),nup(nn),chiex(nn)
        dimension F(nn),CONST(nn),CCC3(nn)
	character fnam(9,nn)
        REAL*8 CCC1,CCC2,CONST,alam,F,CCC3
        REAL*8 ee,cc,me
         open(unit=5,file='Hlinedata.dat',status='old')
         open(unit=7,file='Hydrogen.dat',status='unknown')
         ITOT=124
         pi=3.141615927
         ee=1.6022E-19
         cc=2.997E+08
         me=1.6737236E-24
         xx=10E+24
          CCC1=(pi*ee**2)
          CCC2=cc**2      
         write(6,*)CCC1,CCC2
         do i=1,ITOT
         read(5,100) alam(i),nlow(i),nup(i),chiex(i),F(i),fnam(:,i)
         end do
C         C1=(PI*E**2)/(M*C**2) * CLAM**2 * F*10E24 * 2.06
          do I=1,ITOT
          CCC3(i)=(alam(i))**2
          end do
          do I=1,ITOT
          CONST(i)=CCC1*CCC3(i)*(10**F(i))*2.06*xx/(me*CCC2)
          end do
          
          do I = 1, ITOT
            do J = 1, 9
              if (fnam(J,I) .eq. ' ') fnam(J,I) = '-'
              if (fnam(J,I) .eq. '''') fnam(J,I) = ' '
            end do
          end do
          
          do i=1,ITOT
          write(7,101)fnam(:,i),nlow(i),nup(i),alam(i),chiex(i),CONST(i)
          end do
          stop
 100       FORMAT(1X,F9.3,5X,I1,3X,I2,3X,F6.3,12X,F6.3,4X,A9)
 101       FORMAT(A9,1X,I1,2X,I2,1X,F9.3,3X,F6.3,2X,F12.3)
          end



