%global srcname Imath
%global sover 28

Name:           imath
Version:        3.0.2
Release:        4%{?dist}
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics

License:        BSD
URL:            https://github.com/AcademySoftwareFoundation/Imath
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz


BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  python3-devel
# For documentation generation
BuildRequires:  python3-sphinx
BuildRequires:  python3-breathe

%description
Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D
vectors and matrices and other simple but useful mathematical objects,
functions, and data types common in computer graphics applications, including
the “half” 16-bit floating-point type.


%package -n python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Python module for Imath

%description -n python3-%{name}
%{summary}.


%package devel
Summary:        Development files for Imath
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       python3-devel

%description devel
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%cmake -DPYTHON=ON
%cmake_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/ html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%cmake_install


%check
# https://github.com/AcademySoftwareFoundation/Imath/issues/151
%ifnarch i686
%ctest
%endif


%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_libdir}/libImath-3_0.so.%{sover}*

%files -n python3-%{name}
%{_libdir}/libPyImath_Python3_9-3_0.so.%{sover}*
%{python3_sitearch}/imath.so
%{python3_sitearch}/imathnumpy.so

%files devel
%doc html/
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath.so
%{_libdir}/libImath-3_0.so
%{_libdir}/libPyImath_Python3_9-3_0.so
