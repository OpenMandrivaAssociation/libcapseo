%define major 0
%define libname %mklibname capseo %{major}
%define devname %mklibname capseo -d

# Tarfile created using git
# git clone git://gitorious.org/capseo/mainline.git libcapseo
# cd libcapseo
# git-archive --format=tar --prefix=libcapseo-%{capseo_version}/ %{git_version} | bzip2 > libcapseo-%{capseo_version}-%{gitdate}.tar.bz2

%define gitdate 20081031
%define git_version 431a293

Summary:	A realtime encoder/decoder library
Name:		libcapseo
Version:	0.3.0
Release:	0.%{gitdate}.7
License:	GPLv3+
Group:		System/Libraries
Url:		https://gitorious.org/projects/capseo/
# Specific snapshot no upstream release (yet)
Source0:	%{name}-%{version}-%{gitdate}.tar.bz2
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(theora)

%description
Capseo is a realtime video codec being used by libcaptury/captury
for encoding captured video frames in realtime. (think of FRAPS codec).

Applications using capseo currently are libcaptury for encoding
captured data, e.g. currently from third-party OpenGL applications
via captury, the OpenGL video capturing tool.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 0.3.0-0.20081031.7
Obsoletes:	%{name} < 0.3.0-0.20081031.7

%description -n %{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%doc AUTHORS COPYING TODO
%{_libdir}/libcapseo.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Files needed for development using %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Conflicts:	%{name}-devel < 0.3.0-0.20081031.7
Obsoletes:	%{name}-devel < 0.3.0-0.20081031.7
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/libcapseo.so
%{_libdir}/pkgconfig/capseo.pc

#----------------------------------------------------------------------------

%package tools
Summary:	Encoding/Decoding tools for capseo
Group:		Sound

%description tools
Utilities for capseo.

%files tools
%{_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-theora \
	--disable-examples
%make

%install
%makeinstall_std

