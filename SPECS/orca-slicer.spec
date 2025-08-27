%global tag 2.3.1-alpha
%global version %(tag=%{tag}; echo ${tag//-/_})

Name:           orca-slicer
Version:        %{version}
Release:        1%{?dist}
Summary:        TODO

License:        AGPL-3.0-or-later
URL:            https://github.com/SoftFever/OrcaSlicer
Source0:        https://github.com/SoftFever/OrcaSlicer/archive/refs/tags/%{tag}/OrcaSlicer-%{tag}.tar.gz

BuildRequires: autoconf
BuildRequires: cmake
BuildRequires: curl
BuildRequires: eglexternalplatform-devel
BuildRequires: extra-cmake-modules
BuildRequires: file
BuildRequires: git
BuildRequires: gstreamer1-plugins-bad-free
# BuildRequires: gstreamer1-plugin-libav
BuildRequires: cairo-devel
BuildRequires: libcurl-devel
BuildRequires: dbus-devel
BuildRequires: glew-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gtk3-devel
BuildRequires: libsecret-devel
BuildRequires: libsoup-devel
BuildRequires: openssl-devel
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: wayland-protocols-devel
BuildRequires: webkit2gtk4.1-devel
BuildRequires: libxkbcommon-devel
BuildRequires: glibc-all-langpacks
BuildRequires: tbb-devel
BuildRequires: openvdb-devel

Requires:     hicolor-icon-theme
%description
Orca Slicer is a versatile tool for slicing and preparing 3D models for printing. It supports various file formats and provides advanced features for optimizing print quality.


%prep
tar -xzf %{SOURCE0}
mv OrcaSlicer-%{tag} %{name}-%{version}

%build
cd %{name}-%{version}
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

export CMAKE_C_COMPILER_LAUNCHER=ccache
export CMAKE_CXX_COMPILER_LAUNCHER=ccache
# sed --in-place "s/+UNKNOWN/_$(date '+%F')/" version.inc

rm -rf deps/build
mkdir -p deps/build

echo "XXXXXXXXXX build DEPS"
./build_linux.sh -dr
echo "XXXXXXXXXX build MAIN"
./build_linux.sh -sr
## %cmake -S deps -B deps/build -G Ninja -DDEP_WX_GTK3=ON
##
## echo "XXXXXXXXXX DEPS BUILD"
## cmake --build deps/build -j$(nproc)
##
## echo "XXXXXXXXXX MAIN SETUP -> hacking GLEW path"
## %cmake -S . -B build -G Ninja -DCMAKE_PREFIX_PATH="./deps/build/destdir/usr/local" -DBBL_RELEASE_TO_PUBLIC=1 -DBBL_INTERNAL_TESTING=0 -DSLIC3R_GTK=3 -DSLIC3R_PCH=SLIC3R_PRECOMPILED_HEADERS="ON" -DSLIC3R_STATIC=1 -DORCA_TOOLS=ON
##
## echo "XXXXXXXXXX MAIN BUILD"
## %cmake_build --target OrcaSlicer
##
## echo "XXXXXXXXXX MAIN PROFILE VALIDATOR BUILD"
## %cmake_build --target OrcaSlicer_profile_validator
##
# ./run_gettext.sh

%install
%cmake_install

%files
%license LICENSE.txt
# %doc add-docs-here

%changelog
* Wed Aug 20 2025 Tom von Schwerdtner <tomvons@gmail.com>
- Initial package (by me)
