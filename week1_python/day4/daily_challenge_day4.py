#!/usr/bin/python
# execution : $>python daily_challenge_day4.py

if __name__ == "__main__":
    # Challenge#1
    print("challenge#1: ")
    class Pagination():
        currentPage=1

        def __init__(self, items=None,pageSize=10):
            self.items=items
            self.pageSize=int(pageSize) # nombre d’éléments à afficher sur chaque page (le convertir en int)
            self.totalPages=len(self.items)//self.pageSize+1

        # renvoie une liste d'éléments visibles en fonction de la pageSize
        def getVisibleItems(self):
            #self.totalPages=len(self.items)//self.pageSize

            deb=(self.currentPage-1)*self.pageSize
            fin=deb+self.pageSize

            #print("deb", deb)
            #print("fin", fin)
            #print("totalPages", self.totalPages)
            #print("items", self.items)
            if fin>len(self.items):
                fin=len(self.items)
                deb=len(self.items)-2 # on impose pas possible à (len(self.items)-self.pageSize)

            return [c for c in self.items if deb<=self.items.index(c)<fin]

        #prevPage()
        def prevPage(self):
            self.currentPage -= 1
            return self

        # prevPage()
        def nextPage(self):
            self.currentPage += 1
            return self

        # firstPage()
        def firstPage(self):
            self.currentPage=1
            return self

        # lastPage()
        def lastPage(self):
            self.currentPage=self.totalPages
            return self

        # goToPage(pageNum) et 1<=p.currentPage<=totalPages
        def goToPage(self, pageNum): #le convertir en int
            if int(pageNum)<=0:
                self.currentPage=1 #si 0 ou un nombre négatif est donné, p.currentPage=1
            elif int(pageNum)>len(self.items):
                #self.lastPage()
                self.currentPage=self.totalPages # p.currentPagedoit être définie sur totalPages
            else:
                self.currentPage=pageNum
            return
    # init
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    #print(p.getVisibleItems() )
    assert p.getVisibleItems() == ['a', 'b', 'c', 'd']

    #p.nextPage().nextPage().nextPage().nextPage().nextPage().nextPage()
    p.nextPage()
    #print(p.getVisibleItems() )
    assert p.getVisibleItems()==["e", "f", "g", "h"]

    p.firstPage()
    #print(p.getVisibleItems() )
    assert p.getVisibleItems()==['a', 'b', 'c', 'd']

    p.lastPage()
    #print(p.getVisibleItems() )
    assert p.getVisibleItems()==["y", "z"]

    p.prevPage()
    print("p.prevPage() =>", p.getVisibleItems() )

    # Si page en dehors de totalPages, la méthode goToPage() doit alors accéder à la page la plus proche => lastPage()
    p.goToPage(10)
    print("p.goToPage(10) =>",p.getVisibleItems() )

    print()

#EOF
