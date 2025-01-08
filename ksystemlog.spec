#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksystemlog
Version  : 24.12.0
Release  : 76
URL      : https://download.kde.org/stable/release-service/24.12.0/src/ksystemlog-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/ksystemlog-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/ksystemlog-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: ksystemlog-bin = %{version}-%{release}
Requires: ksystemlog-data = %{version}-%{release}
Requires: ksystemlog-license = %{version}-%{release}
Requires: ksystemlog-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(systemd)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the ksystemlog package.
Group: Binaries
Requires: ksystemlog-data = %{version}-%{release}
Requires: ksystemlog-license = %{version}-%{release}

%description bin
bin components for the ksystemlog package.


%package data
Summary: data components for the ksystemlog package.
Group: Data

%description data
data components for the ksystemlog package.


%package doc
Summary: doc components for the ksystemlog package.
Group: Documentation

%description doc
doc components for the ksystemlog package.


%package license
Summary: license components for the ksystemlog package.
Group: Default

%description license
license components for the ksystemlog package.


%package locales
Summary: locales components for the ksystemlog package.
Group: Default

%description locales
locales components for the ksystemlog package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n ksystemlog-24.12.0
cd %{_builddir}/ksystemlog-24.12.0
pushd ..
cp -a ksystemlog-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735178386
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735178386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksystemlog
cp %{_builddir}/ksystemlog-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ksystemlog/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ksystemlog-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksystemlog/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/ksystemlog-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksystemlog/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ksystemlog-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksystemlog/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ksystemlog
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ksystemlog
/usr/bin/ksystemlog

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksystemlog.desktop
/usr/share/metainfo/org.kde.ksystemlog.appdata.xml
/usr/share/qlogging-categories6/ksystemlog.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/ca/ksystemlog/index.docbook
/usr/share/doc/HTML/de/ksystemlog/filter-process.png
/usr/share/doc/HTML/de/ksystemlog/first-opening.png
/usr/share/doc/HTML/de/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/de/ksystemlog/index.docbook
/usr/share/doc/HTML/de/ksystemlog/main-screen.png
/usr/share/doc/HTML/en/ksystemlog/filter-process.png
/usr/share/doc/HTML/en/ksystemlog/first-opening.png
/usr/share/doc/HTML/en/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/en/ksystemlog/index.docbook
/usr/share/doc/HTML/en/ksystemlog/main-screen.png
/usr/share/doc/HTML/es/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/es/ksystemlog/index.docbook
/usr/share/doc/HTML/et/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/et/ksystemlog/index.docbook
/usr/share/doc/HTML/fr/ksystemlog/filter-process.png
/usr/share/doc/HTML/fr/ksystemlog/first-opening.png
/usr/share/doc/HTML/fr/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/fr/ksystemlog/index.docbook
/usr/share/doc/HTML/fr/ksystemlog/main-screen.png
/usr/share/doc/HTML/it/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/it/ksystemlog/index.docbook
/usr/share/doc/HTML/ko/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/ko/ksystemlog/index.docbook
/usr/share/doc/HTML/nl/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/nl/ksystemlog/index.docbook
/usr/share/doc/HTML/pt/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/pt/ksystemlog/index.docbook
/usr/share/doc/HTML/pt_BR/ksystemlog/filter-process.png
/usr/share/doc/HTML/pt_BR/ksystemlog/first-opening.png
/usr/share/doc/HTML/pt_BR/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksystemlog/index.docbook
/usr/share/doc/HTML/pt_BR/ksystemlog/main-screen.png
/usr/share/doc/HTML/ru/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/ru/ksystemlog/index.docbook
/usr/share/doc/HTML/sl/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/sl/ksystemlog/index.docbook
/usr/share/doc/HTML/sv/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/sv/ksystemlog/index.docbook
/usr/share/doc/HTML/tr/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/tr/ksystemlog/index.docbook
/usr/share/doc/HTML/uk/ksystemlog/filter-process.png
/usr/share/doc/HTML/uk/ksystemlog/first-opening.png
/usr/share/doc/HTML/uk/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/uk/ksystemlog/index.docbook
/usr/share/doc/HTML/uk/ksystemlog/main-screen.png
/usr/share/doc/HTML/zh_CN/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/zh_CN/ksystemlog/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksystemlog/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ksystemlog/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/ksystemlog/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ksystemlog/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f ksystemlog.lang
%defattr(-,root,root,-)

