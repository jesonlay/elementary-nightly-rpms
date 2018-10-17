%global srcname greeter
%global appname io.elementary.%{srcname}

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        3.2.0+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz
Source1:        40-%{appname}.conf
Source2:        %{appname}.whitelist

# Remove gsettings stuff that's no longer there and causes crashes
Patch0:         00-disable-gsettings.patch

# Set default wallpaper to the default location on fedora
Patch1:         01-set-default-wallpaper.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(mutter-clutter-2)
BuildRequires:  pkgconfig(mutter-cogl-2)
BuildRequires:  pkgconfig(mutter-cogl-pango-2)
BuildRequires:  pkgconfig(mutter-cogl-path-2)
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(x11)

Provides:       pantheon-greeter = %{version}-%{release}
Obsoletes:      pantheon-greeter


Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# Raleway font is used for interface elements
Requires:       impallari-raleway-fonts

# Runtime requirement for numlock capture
Requires:       numlockx

# Requirement for default wallpaper
Requires:       elementary-wallpapers


# All LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# Alternate, more descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}


%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# Install LightDM configuration file
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/

# Install wingpanel overrides for the greeter
mkdir -p %{buildroot}%{_sysconfdir}/wingpanel.d
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/wingpanel.d


%files -f %{appname}.lang
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf
%config(noreplace) %{_sysconfdir}/wingpanel.d/%{appname}.whitelist

%{_bindir}/%{appname}-compositor

%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop


%changelog
* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 3.2.0+git181017.182232.cbfbca98-2
- Renamed package from pantheon-greeter.

