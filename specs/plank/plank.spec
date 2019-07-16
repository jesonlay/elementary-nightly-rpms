%global common_description %{expand:
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.}

Name:           plank
Summary:        Stupidly simple Dock
Version:        0.11.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://launchpad.net/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext >= 0.19.6
BuildRequires:  gettext-devel >= 0.19.6
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.34.0

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.4.0
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       bamf-daemon
Requires:       hicolor-icon-theme

%description %{common_description}


%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}
This package contains the shared libraries.


%package        docklets
Summary:        Docklets for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    docklets %{common_description}
This package contains the docklets for plank.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}
This package contains the files necessary to develop against plank.


%prep
%autosetup -p1


%build
autoreconf -vfi
%configure --disable-apport
%make_build


%install
%make_install

%find_lang %{name}

# remove libtool archives from the buildroot
find %{buildroot} -name "*.la" -print -delete


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc AUTHORS

%{_bindir}/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}/

%{_mandir}/man1/%{name}.1*


%files libs
%license COPYING
%doc AUTHORS

%{_libdir}/lib%{name}.so.1*

%dir %{_libdir}/%{name}


%files docklets
%license COPYING
%doc AUTHORS

%dir %{_libdir}/%{name}/docklets
%{_libdir}/%{name}/docklets/*.so


%files devel
%license COPYING
%doc AUTHORS

%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_includedir}/%{name}/

%{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/vala/vapi/%{name}.deps


%changelog
* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 0.11.4+git190505.155400.96bbb1d2-1
- Initial packaging for snapshot builds.

