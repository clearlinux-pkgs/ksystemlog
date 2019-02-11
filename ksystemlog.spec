#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ksystemlog
Version  : 18.12.2
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.2/src/ksystemlog-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/ksystemlog-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/ksystemlog-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ksystemlog-bin = %{version}-%{release}
Requires: ksystemlog-data = %{version}-%{release}
Requires: ksystemlog-license = %{version}-%{release}
Requires: ksystemlog-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(systemd)

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
%setup -q -n ksystemlog-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549874840
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549874840
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksystemlog
cp COPYING %{buildroot}/usr/share/package-licenses/ksystemlog/COPYING
pushd clr-build
%make_install
popd
%find_lang ksystemlog

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksystemlog

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksystemlog.desktop
/usr/share/kxmlgui5/ksystemlog/ksystemlogui.rc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksystemlog/filter-process.png
/usr/share/doc/HTML/ca/ksystemlog/first-opening.png
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
/usr/share/doc/HTML/nl/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/nl/ksystemlog/index.docbook
/usr/share/doc/HTML/pt/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/pt/ksystemlog/index.docbook
/usr/share/doc/HTML/pt_BR/ksystemlog/filter-process.png
/usr/share/doc/HTML/pt_BR/ksystemlog/first-opening.png
/usr/share/doc/HTML/pt_BR/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksystemlog/index.docbook
/usr/share/doc/HTML/pt_BR/ksystemlog/main-screen.png
/usr/share/doc/HTML/sv/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/sv/ksystemlog/index.docbook
/usr/share/doc/HTML/uk/ksystemlog/filter-process.png
/usr/share/doc/HTML/uk/ksystemlog/first-opening.png
/usr/share/doc/HTML/uk/ksystemlog/index.cache.bz2
/usr/share/doc/HTML/uk/ksystemlog/index.docbook
/usr/share/doc/HTML/uk/ksystemlog/main-screen.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksystemlog/COPYING

%files locales -f ksystemlog.lang
%defattr(-,root,root,-)

