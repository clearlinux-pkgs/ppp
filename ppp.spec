#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ppp
Version  : 2.4.8
Release  : 13
URL      : https://github.com/paulusmack/ppp/archive/ppp-2.4.8.tar.gz
Source0  : https://github.com/paulusmack/ppp/archive/ppp-2.4.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 RSA-MD
Requires: ppp-bin = %{version}-%{release}
Requires: ppp-lib = %{version}-%{release}
Requires: ppp-license = %{version}-%{release}
Requires: ppp-man = %{version}-%{release}
BuildRequires : openssl-dev
Patch1: triple-rot13.patch
Patch2: CVE-2020-8597.patch
Patch3: use-system-cflags.patch

%description
Point-to-Point Protocol (PPP) to provide Internet connections over
serial lines.

%package bin
Summary: bin components for the ppp package.
Group: Binaries
Requires: ppp-license = %{version}-%{release}

%description bin
bin components for the ppp package.


%package dev
Summary: dev components for the ppp package.
Group: Development
Requires: ppp-lib = %{version}-%{release}
Requires: ppp-bin = %{version}-%{release}
Provides: ppp-devel = %{version}-%{release}
Requires: ppp = %{version}-%{release}

%description dev
dev components for the ppp package.


%package lib
Summary: lib components for the ppp package.
Group: Libraries
Requires: ppp-license = %{version}-%{release}

%description lib
lib components for the ppp package.


%package license
Summary: license components for the ppp package.
Group: Default

%description license
license components for the ppp package.


%package man
Summary: man components for the ppp package.
Group: Default

%description man
man components for the ppp package.


%prep
%setup -q -n ppp-ppp-2.4.8
cd %{_builddir}/ppp-ppp-2.4.8
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604876095
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}  COPTS="$CFLAGS"

%install
export SOURCE_DATE_EPOCH=1604876095
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ppp
cp %{_builddir}/ppp-ppp-2.4.8/pppd/plugins/pppoatm/COPYING %{buildroot}/usr/share/package-licenses/ppp/18bfbcc612f7daaeb150e2ef5dad0aec82b80b51
cp %{_builddir}/ppp-ppp-2.4.8/pppd/plugins/radius/COPYRIGHT %{buildroot}/usr/share/package-licenses/ppp/b98c076b7b97562c420880d0d45ec541b7410f9f
%make_install DESTDIR=%{buildroot}/usr
## install_append content
chmod 0755 %{buildroot}/usr/lib/pppd/2.4.8/*.so
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chat
/usr/bin/pppd
/usr/bin/pppdump
/usr/bin/pppoe-discovery
/usr/bin/pppstats

%files dev
%defattr(-,root,root,-)
/usr/include/pppd/ccp.h
/usr/include/pppd/chap-new.h
/usr/include/pppd/chap_ms.h
/usr/include/pppd/eap.h
/usr/include/pppd/ecp.h
/usr/include/pppd/eui64.h
/usr/include/pppd/fsm.h
/usr/include/pppd/ipcp.h
/usr/include/pppd/ipv6cp.h
/usr/include/pppd/ipxcp.h
/usr/include/pppd/lcp.h
/usr/include/pppd/magic.h
/usr/include/pppd/md4.h
/usr/include/pppd/md5.h
/usr/include/pppd/patchlevel.h
/usr/include/pppd/pathnames.h
/usr/include/pppd/pppcrypt.h
/usr/include/pppd/pppd.h
/usr/include/pppd/session.h
/usr/include/pppd/sha1.h
/usr/include/pppd/spinlock.h
/usr/include/pppd/tdb.h
/usr/include/pppd/upap.h

%files lib
%defattr(-,root,root,-)
/usr/lib/pppd/2.4.8/minconn.so
/usr/lib/pppd/2.4.8/openl2tp.so
/usr/lib/pppd/2.4.8/passprompt.so
/usr/lib/pppd/2.4.8/passwordfd.so
/usr/lib/pppd/2.4.8/pppoatm.so
/usr/lib/pppd/2.4.8/pppol2tp.so
/usr/lib/pppd/2.4.8/radattr.so
/usr/lib/pppd/2.4.8/radius.so
/usr/lib/pppd/2.4.8/radrealms.so
/usr/lib/pppd/2.4.8/rp-pppoe.so
/usr/lib/pppd/2.4.8/winbind.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ppp/18bfbcc612f7daaeb150e2ef5dad0aec82b80b51
/usr/share/package-licenses/ppp/b98c076b7b97562c420880d0d45ec541b7410f9f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/chat.8
/usr/share/man/man8/pppd-radattr.8
/usr/share/man/man8/pppd-radius.8
/usr/share/man/man8/pppd.8
/usr/share/man/man8/pppdump.8
/usr/share/man/man8/pppstats.8
