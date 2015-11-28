#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

Summary:        KBlog - a blogging library for KDE
Name:           kblog
Version:	15.08.3
Release:	1
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/


BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5XmlRpcClient)

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
%_libdir/libKF5Blog.so.%{kblog_major}*
%_libdir/libKF5Blog.so.5

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
%_includedir/KF5/KBlog
%_includedir/KF5/*.h
%_libdir/*.so
%_libdir/cmake/KF5Blog
%_libdir/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build


