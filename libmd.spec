Summary:	Message digest library
Summary(pl.UTF-8):	Biblioteka skrótów wiadomości (Message Digest)
Name:		libmd
Version:	0.3
Release:	2
License:	RSA non-commercial (MD2), RSA BSD-like (MD4), Public Domain (MD5)
Group:		Libraries
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/libmd/%{name}-%{version}.tar.bz2
# Source0-md5:	1db1795b7e87bbda542e4c33b6ce5566
Patch0:		%{name}-install.patch
URL:		http://martin.hinner.info/libmd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmd is a cryptographic message digest library. It implements these
message digest algorithms:
 - MD2 (RFC 1319 - B. Kaliski)
 - MD4 (RFC 1186 - R. Rivest)
 - MD5 (RFC 1321 - R. Rivest)
 - SHA-1 (FIPS PUB 180 and 180.1 - NIST)
 - RIPEMD-160 <http://www.esat.kuleuven.ac.be/~bosselae/ripemd160.html>

%description -l pl.UTF-8
Libmd to biblioteka kryptograficznych skrótów wiadomości. Implementuje
następujące algorytmy skrótów wiadomości:
 - MD2 (RFC 1319 - B. Kaliski)
 - MD4 (RFC 1186 - R. Rivest)
 - MD5 (RFC 1321 - R. Rivest)
 - SHA-1 (FIPS PUB 180 oraz 180.1 - NIST)
 - RIPEMD-160 <http://www.esat.kuleuven.ac.be/~bosselae/ripemd160.html>

%package devel
Summary:	Header files for libmd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmd.

%package static
Summary:	Static libmd library
Summary(pl.UTF-8):	Statyczna biblioteka libmd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmd library.

%description static -l pl.UTF-8
Statyczna biblioteka libmd.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure

%{__make} \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC -I."

%{__make} -C docs libmd.txt

%install
rm -rf $RPM_BUILD_ROOT

# install headers to include/libmd to avoid too common filenames under /usr/include
%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT \
	includedir=%{_includedir}/libmd \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO md2.copyright md4.copyright md5.copyright
%attr(755,root,root) %{_libdir}/libmd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmd.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/libmd.txt docs/algorithms
%attr(755,root,root) %{_libdir}/libmd.so
%{_includedir}/libmd
%{_mandir}/man3/md2.3*
%{_mandir}/man3/md4.3*
%{_mandir}/man3/md5.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmd.a
