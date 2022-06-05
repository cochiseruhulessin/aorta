# The name of this Python package, or the parent package if this is a
# namespaced package.
PYTHON_PKG_NAME=aorta

# The subpackage name in a packaging namespace.
#PYTHON_SUBPKG_NAME=

# Choose from 'application' or 'package'.
PROJECT_KIND=package

# Choose from 'parent' or 'namespaced'. If you are not sure, choose 'parent'.
# If PROJECT_SCOPE=namespaced, then PYTHON_SUBPKG_NAME must also be set.
PROJECT_SCOPE=parent

# The Python version to use.
PYTHON_VERSION = 3.10

# Tables to truncate when invoking `make dbtruncate`, separated by a space.
#RDBMS_TRUNCATE=

# Components to configure.
mk.configure += python python-docs python-gitlab docker python-package
mk.configure +=

# User-defined environment variables
LOG_LEVEL=DEBUG
LOGLEVEL=DEBUG
OAUTH2_ACTOR_KEY=pki/pkcs/noop.rsa
OAUTH2_TRUSTED_STS=self
OS_RELEASE_ID ?= debian
OS_RELEASE_VERSION ?= 10
TEST_MIN_COVERAGE = 70
