#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        KBlog - a blogging library for KDE
Name:           kblog
Version: 15.08.0
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/


BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)

BuildRequires:  kf5-macros
BuildRequires:  kdelibs4support-devel >= 5.12.0
BuildRequires:  kio-devel >= 5.12.0
BuildRequires:  kcoreaddons-devel >= 5.12.0
BuildRequires:  kxmlrpcclient-devel 
BuildRequires:  syndication-devel >= 4.79.0
BuildRequires:  kcalcore-devel >= 4.79.0

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
KBlog - a blogging library for KDE

#--------------------------------------------------------------------

%define kblog_major 4
%define libkblog %mklibname kf5blog %{kblog_major}

%package -n %libkblog
Summary:      KBlog - a blogging library for KDE
Group:        System/Libraries


%description -n %libkblog
KBlog - a blogging library for KDE

%files -n %libkblog
%_kf5_libdir/libKF5Blog.so.%{kblog_major}*
%_kf5_libdir/libKF5Blog.so.5

#--------------------------------------------------------------------

%define kblog_devel %mklibname kblog -d

%package -n %kblog_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkblog = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kblog_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kblog_devel
%_kf5_includedir/KBlog
%_kf5_includedir/*.h
%_kf5_libdir/*.so
%_kf5_libdir/cmake/KF5Blog
%_qt5_prefix/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build

%find_lang --all %{name}5



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865923
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 864000
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861736
- New version 15.07.90

* Wed Jul 29 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 858858
- imported package kblog

