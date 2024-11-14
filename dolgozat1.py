szó= input("Kérek egy szót: ")

if "s" in szó and "c" in szó:
    print(f"A {szó}-ban van s és c betű is.")
elif "s" in szó or "c" in szó:
    print(f"A {szó}-ban van s vagy c betű.")
else:
    print(f"A {szó}-ban nincs se c se s betű.")
