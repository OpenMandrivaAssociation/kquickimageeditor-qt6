%undefine gitdate

%define devname %mklibname %{name} -d

Name:		kquickimageeditor-qt6
Version:	0.5.1
Release:	%{?gitdate:0.%{gitdate}.}1
Summary:	Qt Image editing components
License:	LGPL2.1
Group:		System/Libraries
Url:		https://invent.kde.org/libraries/kquickimageeditor
%if 0%{?gitdate}
Source0:	https://invent.kde.org/libraries/kquickimageeditor/-/archive/master/%{name}-master.tar.bz2
%else
#Source0:	https://invent.kde.org/libraries/kquickimageeditor/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source0:	https://download.kde.org/stable/kquickimageeditor/kquickimageeditor-%{version}.tar.xz
%endif

BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Designer)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Qml)

%description
QML Component for image editing

%package -n %{devname}
Summary:	Header files for KQuickImageEditor
Group:		Development/C
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Header files of for KQuickImageEditor.

%prep
%autosetup -p1 -n kquickimageeditor-%{version}
%cmake \
       -DBUILD_WITH_QT6:BOOL=ON \
       -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
       -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
# Don't clash with the qt5 version
mkdir -p %{buildroot}%{_qtdir}/lib/cmake
mv %{buildroot}%{_libdir}/cmake/KQuickImageEditor %{buildroot}%{_qtdir}/lib/cmake

%files
%{_qtdir}/qml/org/kde/kquickimageeditor

%files -n %{devname}
%{_qtdir}/mkspecs/modules/qt_KQuickImageEditor.pri
%{_qtdir}/lib/cmake/KQuickImageEditor
