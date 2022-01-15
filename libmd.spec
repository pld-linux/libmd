Summary:	Message Digest functions from BSD systems
Summary(pl.UTF-8):	Funkcje skrótów wiadomości (MD) z systemów BSD
Name:		libmd
Version:	1.0.4
Release:	1
License:	BSD, ISC, Public Domain
Group:		Libraries
Source0:	https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	e8e955f8d53d2c9306b07c90ff6ae395
URL:		https://www.hadrons.org/software/libmd/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	libmd-bsd < 1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides message digest functions found on BSD systems
either on their libc or libmd libraries and lacking on others like GNU
systems, thus making it easier to port projects with strong BSD
origins, without needing to embed the same code over and over again on
each project.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje skrótów wiadomości spotykane w
systemach BSD w bibliotece libc lub libmd, a nie występujące na
innych systemach, takich jak GNU. Dzięki temu ułatwia portowanie
projektów mających silne korzenie BSD bez potrzeby osadzania ciągle
tego samego kodu w każdym projekcie.

%package devel
Summary:	Header files for BSD MD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BSD MD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmd-bsd-devel < 1.0.4

%description devel
Header files for BSD MD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BSD MD.

%package static
Summary:	Static BSD MD library
Summary(pl.UTF-8):	Statyczna biblioteka BSD MD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libmd-bsd-static < 1.0.4

%description static
Static BSD MD library.

%description static -l pl.UTF-8
Statyczna biblioteka BSD MD.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--includedir=%{_includedir}/libmd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmd.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmd.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmd.so
%{_includedir}/libmd
%{_pkgconfigdir}/libmd.pc
%{_mandir}/man3/MD2*.3*
%{_mandir}/man3/MD4*.3*
%{_mandir}/man3/MD5*.3*
%{_mandir}/man3/RMD160*.3*
%{_mandir}/man3/SHA1*.3*
%{_mandir}/man3/SHA256*.3*
%{_mandir}/man3/SHA384*.3*
%{_mandir}/man3/SHA512*.3*
%{_mandir}/man3/md2.3*
%{_mandir}/man3/md4.3*
%{_mandir}/man3/md5.3*
%{_mandir}/man3/rmd160.3*
%{_mandir}/man3/sha1.3*
%{_mandir}/man3/sha2.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmd.a
