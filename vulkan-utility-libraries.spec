%global debug_package %{nil}

Name:           vulkan-utility-libraries
Version:        1.4.350
Release:        1
Summary:        Vulkan utility libraries
Group:		Libraries
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source0:        %url/archive/Vulkan-Utility-Libraries-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	make
BuildRequires:  python-devel
BuildRequires:  vulkan-headers

Provides:       vulkan-validation-layers-devel = %{version}-%{release}

%description
%{summary}


%prep
%autosetup -p1 -n Vulkan-Utility-Libraries-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DBUILD_TESTS:BOOL=OFF \
       -DVUL_WERROR:BOOL=OFF \
       -DUPDATE_DEPS:BOOL=OFF
%make_build

%install
%make_install -C build

%files
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a

