%define capseo_version 0.3.0

# Tarfile created using git
# git clone git://gitorious.org/capseo/mainline.git libcapseo
# cd libcapseo
# git-archive --format=tar --prefix=libcapseo-%{capseo_version}/ %{git_version} | bzip2 > libcapseo-%{capseo_version}-%{gitdate}.tar.bz2

%define gitdate 20081031
%define git_version 431a293

%define tarfile %{name}-%{capseo_version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}

Summary:        A realtime encoder/decoder library
Name:           libcapseo
Version:        %{capseo_version}
Release:        %mkrel 0.%{snapshot}.6
License:        GPLv3
Group:          System/Libraries 
URL:            http://gitorious.org/projects/capseo/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  mesagl-devel
BuildRequires:	libtheora-devel
BuildRequires:	libogg-devel
# Specific snapshot no upstream release (yet)
Source0:        %{tarfile}

%description
Capseo is a realtime video codec being used by libcaptury/captury
for encoding captured video frames in realtime. (think of FRAPS codec).

Applications using capseo currently are libcaptury for encoding
captured data, e.g. currently from third-party OpenGL applications
via captury, the OpenGL video capturing tool.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO
%{_libdir}/*.so.*

#--------------------------------------------------------------------

%package devel
Summary: Files needed for development using %{name}
Group:    Development/Other 
Requires: %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/libcapseo.so
%{_libdir}/pkgconfig/capseo.pc

#--------------------------------------------------------------------

%package tools
Summary: Encoding/Decoding tools for capseo
Group:   Sound
Requires: %{name} = %{version}-%{release}

%description tools
Utilities for capseo

%files tools
%defattr(-,root,root,-)
%{_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x --disable-static --enable-theora --disable-examples
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}/%{_libdir}/*.la

%clean
rm -rf %{buildroot}


%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.3.0-0.20081031.6mdv2011.0
+ Revision: 636024
- BR ogg
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.20081031.5mdv2011.0
+ Revision: 620084
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-0.20081031.4mdv2010.0
+ Revision: 438523
- rebuild

* Fri Dec 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.0-0.20081031.3mdv2009.1
+ Revision: 316043
- Fix  Requires

* Thu Dec 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.0-0.20081031.2mdv2009.1
+ Revision: 315994
- Fix groups
- import libcapseo


