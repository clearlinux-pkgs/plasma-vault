#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-vault
Version  : 5.18.5
Release  : 35
URL      : https://download.kde.org/stable/plasma/5.18.5/plasma-vault-5.18.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.18.5/plasma-vault-5.18.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.18.5/plasma-vault-5.18.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: plasma-vault-data = %{version}-%{release}
Requires: plasma-vault-lib = %{version}-%{release}
Requires: plasma-vault-license = %{version}-%{release}
Requires: plasma-vault-locales = %{version}-%{release}
BuildRequires : NetworkManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev
BuildRequires : libksysguard-dev
BuildRequires : plasma-framework-dev

%description
Plasma Applet mixed C++/QML Template
----------------------
-- Build instructions --

%package data
Summary: data components for the plasma-vault package.
Group: Data

%description data
data components for the plasma-vault package.


%package lib
Summary: lib components for the plasma-vault package.
Group: Libraries
Requires: plasma-vault-data = %{version}-%{release}
Requires: plasma-vault-license = %{version}-%{release}

%description lib
lib components for the plasma-vault package.


%package license
Summary: license components for the plasma-vault package.
Group: Default

%description license
license components for the plasma-vault package.


%package locales
Summary: locales components for the plasma-vault package.
Group: Default

%description locales
locales components for the plasma-vault package.


%prep
%setup -q -n plasma-vault-5.18.5
cd %{_builddir}/plasma-vault-5.18.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588706063
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1588706063
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-vault
cp %{_builddir}/plasma-vault-5.18.5/COPYING %{buildroot}/usr/share/package-licenses/plasma-vault/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/plasma-vault-5.18.5/COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/plasma-vault/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/plasma-vault-5.18.5/COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-vault/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang plasmavault-kde

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/plasma-applet-org.kde.plasma.vault.desktop
/usr/share/metainfo/org.kde.plasma.vault.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/contents/ui/ActionItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/contents/ui/VaultItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.vault/metadata.json

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kded/plasmavault.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/plasmavaultfileitemaction.so
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_vault.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-vault/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/plasma-vault/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/plasma-vault/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f plasmavault-kde.lang
%defattr(-,root,root,-)

