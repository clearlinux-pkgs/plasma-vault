#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-vault
Version  : 5.22.1
Release  : 49
URL      : https://download.kde.org/stable/plasma/5.22.1/plasma-vault-5.22.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.22.1/plasma-vault-5.22.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.22.1/plasma-vault-5.22.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
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
%setup -q -n plasma-vault-5.22.1
cd %{_builddir}/plasma-vault-5.22.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623814199
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
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623814199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-vault
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/plasma-vault-5.22.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/plasma-vault-5.22.1/plasma/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/plasma-vault-5.22.1/plasma/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/plasma-vault-5.22.1/plasma/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/plasma-vault-5.22.1/plasma/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
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
/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-vault/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-vault/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasmavault-kde.lang
%defattr(-,root,root,-)

