Summary:	The Plastic File System
Summary(pl.UTF-8):	Plastyczny system plików
Name:		plasticfs
Version:	1.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://plasticfs.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	533dccd31ebcc6095e3c70663235a0fe
URL:		http://plasticfs.sourceforge.net/
BuildRequires:	groff
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Plastic File System is an LD_PRELOAD module for manipulating what
the file system looks like for programs. This allows virtual file
systems to exist in user space, without kernel hacks or modules.

%description -l pl.UTF-8
Plastic File System to wczytywany przez LD_PRELOAD moduł do
manipulowania wyglądem systemu plików dla programów. Pozwala na
istnienie wirtualnych systemów plików w przestrzeni użytkownika, bez
żadnych modyfikacji w jądrze ani modułów jądra.

%package devel
Summary:	Header files for plasticfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki plasticfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for plasticfs library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki plasticfs.

%package static
Summary:	Static plasticfs library
Summary(pl.UTF-8):	Statyczna biblioteka plasticfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static plasticfs library.

%description static -l pl.UTF-8
Statyczna biblioteka plasticfs.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	RPM_BUILD_ROOT=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_mandir}/man1/plasticfs_license.1*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc etc/README.man
%attr(755,root,root) %{_libdir}/libplasticfs.so.*.*.*
%{_mandir}/man3/plasticfs.3*
%{_mandir}/manl/plasticfs_*.l*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
