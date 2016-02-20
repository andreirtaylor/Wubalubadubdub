import pkgutil, sys, os

tests = []

dirname = os.path.dirname(os.path.realpath(__file__))
for importer, package_name, _ in pkgutil.iter_modules([dirname]):
    full_package_name = '%s.%s' % (dirname, package_name)
    if full_package_name not in sys.modules:
        module = importer.find_module(package_name
                ).load_module(full_package_name)
        #print module
        tests.append(module)

def get(dirname = os.path.dirname(os.path.realpath(__file__))):
    return tests

