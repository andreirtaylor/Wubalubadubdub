import pkgutil, sys, os

tests = []

dirname = os.path.dirname(os.path.realpath(__file__))

for importer, package_name, _ in pkgutil.iter_modules([dirname]):
    full_package_name = '%s.%s' % (dirname, package_name)

    if full_package_name in sys.modules:
        raise NameError("Dont name your test the name of a python module")

    module = importer.find_module(package_name
            ).load_module(full_package_name)
    tests.append(module)

def get(dirname = os.path.dirname(os.path.realpath(__file__))):
    return tests

def print_tests():
    print "\nCurrent Tests\n" 
    print "Name  \t Weight" 
    for test in get():
        print os.path.basename(test.__file__).replace(".pyc", "") + " \t " + str(test.WEIGHT)
    print "\n"

