%global major 29
%global api 3_1

%define devname	%mklibname %{name} -d
%define libname	%mklibname Imath

%define oldlibname %mklibname Imath 3_1 29
%define olderlibname %mklibname Imath 3_0 28

Name:		Imath
Version:	3.2.2
Release:	1
Summary:	Library of 2D and 3D vector, matrix, and math operations for computer graphics
License:	BSD
URL:		https://github.com/AcademySoftwareFoundation/Imath
Source0:	https://github.com/AcademySoftwareFoundation/Imath/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	boost-numpy-devel
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	pkgconfig(python3)
BuildRequires:  python
BuildRequires:  pkgconfig(pybind11)
# For documentation generation
#BuildRequires:  python-sphinx
#BuildRequires:  python-breathe

%description
Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D
vectors and matrices and other simple but useful mathematical objects,
functions, and data types common in computer graphics applications, including
the “half” 16-bit floating-point type.

%package -n %{libname}
Summary:	libraries from Imath
Group:		System/Libraries
%rename %{oldlibname}
Obsoletes:	%{olderlibname} < 3.1.0-0

%description -n %{libname}
Libraries from Imath.

%package -n python-%{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{libname}%{?_isa} = %{version}-%{release}
Summary:	Python module for Imath

%description -n python-%{name}
%{summary}.

%package -n %{devname}
Summary:	Development files for Imath
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{libname}%{?_isa} = %{version}-%{release}
Requires:	python-%{name}%{?_isa} = %{version}-%{release}
Requires:	boost-devel
Requires:	python-devel
Provides:	Imath-devel = %{EVRD}
Provides:	imath-devel = %{EVRD}

# We can't coexist with the old ilmbase (same libImath.so filename)
# but it can coexist in the same repo for the time being...
Obsoletes:	%{_lib}ilmbase2_5-devel < 3.0.0-0

%description -n %{devname}
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cmake -DPYTHON=ON -DPython3_LIBRARY=/usr/lib64/libpython3.11.so -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md

%files -n %{libname}
%{_libdir}/libImath-%{api}.so.%{major}*

%files -n python-%{name}
%{_libdir}/libPyImath_Python*_*-%{api}.so.%{major}*
%{python3_sitearch}/imath.so
%{python3_sitearch}/imathnumpy.so

%files -n %{devname}
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath.so
%{_libdir}/libImath-%{api}.so
%{_libdir}/libPyImath_Python*_*-%{api}.so
