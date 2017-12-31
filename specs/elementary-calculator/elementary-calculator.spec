%global srcname calculator
%global appname io.elementary.calculator

Name:           elementary-calculator
Summary:        Tiny, simple calculator written in GTK+ and Vala
Version:        0.1.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6

Provides:       pantheon-calculator
Obsoletes:      pantheon-calculator


%description
A tiny, simple calculator written in GTK+ and Vala.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# FIXME Remove extra.mo files that shouldn't be installed, meson bug
find %{buildroot} -name "extra.mo" -print -delete


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc AUTHORS
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171116.231410.81be3d74-1
- Initial package.


