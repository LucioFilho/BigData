def thinking_super_means_parent():
    class Root:
        def f(self):
            print("Root.f")

    class A(Root):
        def f(self):
            print("A.f")
            super().f()

    class B(Root):
        def f(self):
            print("B.f")
            super().f()

    class C(A, B):
        def f(self):
            print("C.f")
            super().f()

    C().f()
    # C.f
    # A.f
    # B.f
    # Root.f

    print([cls.__name__ for cls in C.__mro__]) # C, A, B, Root, object
