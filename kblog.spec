#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

Summary:        KBlog - a blogging library for KDE
Name:           kblog
Version:	20.04.1
Release:	1
License:        GPLv2+
Group:          System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/


BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)

BuildRequires:  cmake(ECM)
BuildRequires:	cmake(KF5Auth)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5XmlRpcClient)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%define kblog_major 5
%define libkblog %mklibname kf5blog %{kblog_major}

Requires:	%{libkblog} = %{EVRD}

%description
KBlog - a blogging library for KDE

%files -f libkblog5.lang
%{_datadir}/qlogging-categories5/kblog.categories
%{_datadir}/qlogging-categories5/kblog.renamecategories

#--------------------------------------------------------------------

%package -n %libkblog
Summary:      KBlog - a blogging library for KDE
Group:        System/Libraries
Obsoletes:    %mklibname kf5blog 4
Requires:     %{name} = %{EVRD}

%description -n %libkblog
KBlog - a blogging library for KDE

%files -n %libkblog
%_libdir/libKF5Blog.so.%{kblog_major}*

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
%autopatch -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang libkblog5
