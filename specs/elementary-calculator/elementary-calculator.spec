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
* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180308.183644.a7c0a2a3-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.214634.17b3591b-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.202642.882b2b23-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180306.190254.0e97a7fe-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180225.145705.6cca8d6e-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180205.001047.f528b042-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180128.000728.37803bca-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180104.232914.aff8bd5e-2
- Clean up .spec file.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180104.232914.aff8bd5e-1
- Update to latest snapshot.

* Sun Dec 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171116.231410.81be3d74-1
- Initial package.


