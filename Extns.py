filename = input("Enter the filename : ");
f_exts=filename.split(".");
print("The extension used here is "+repr(f_exts[-1]));
if(f_exts == py)
{ print("This is file of Python programe ");
}
else if(f_exts == java)
{ print("file is of Java programe ");
}
else if(f_exts == c)
{ print("file is of C-programe ");
}
else if(f_exts == cpp)
{ print("file is of C++ programe ");
}
else
{ print("invalid extension ");
}
