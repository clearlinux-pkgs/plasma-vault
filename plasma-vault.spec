#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-vault
Version  : 6.1.5
Release  : 103
URL      : https://download.kde.org/stable/plasma/6.1.5/plasma-vault-6.1.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.5/plasma-vault-6.1.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.5/plasma-vault-6.1.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: plasma-vault-data = %{version}-%{release}
Requires: plasma-vault-lib = %{version}-%{release}
Requires: plasma-vault-license = %{version}-%{release}
Requires: plasma-vault-locales = %{version}-%{release}
BuildRequires : NetworkManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : libksysguard-dev
BuildRequires : networkmanager-qt-dev
BuildRequires : plasma-activities-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-vault-6.1.5
cd %{_builddir}/plasma-vault-6.1.5
pushd ..
cp -a plasma-vault-6.1.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725998575
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
export SOURCE_DATE_EPOCH=1725998575
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-vault
cp %{_builddir}/plasma-vault-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-vault/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-vault-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-vault-%{version}/plasma/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-vault-%{version}/plasma/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-vault-%{version}/plasma/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-vault-%{version}/plasma/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275 || :
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
%find_lang plasmavault-kde
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/org.kde.plasma.vault.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/contents/ui/VaultItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.vault/metadata.json

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/kf6/kded/plasmavault.so
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/plasmavaultfileitemaction.so
/V3/usr/lib64/qt6/plugins/plasma/applets/org.kde.plasma.vault.so
/usr/lib64/qt6/plugins/kf6/kded/plasmavault.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/plasmavaultfileitemaction.so
/usr/lib64/qt6/plugins/plasma/applets/org.kde.plasma.vault.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-vault/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-vault/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/plasma-vault/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-vault/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-vault/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-vault/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma-vault/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasmavault-kde.lang
%defattr(-,root,root,-)

