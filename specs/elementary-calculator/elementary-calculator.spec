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
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.235019.b812cc2d-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.085326.e456d719-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180522.000819.9725c684-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180514.154020.8a3431b9-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180513.163946.db333c6e-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180508.203340.5a8c2945-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180507.000209.dab2b320-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180416.000850.839769e8-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180326.000821.33ddff8e-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180320.001100.1b1508e5-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180318.010025.9cc6da68-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180308.183644.a7c0a2a3-2
- Adapt to upstream file changes.

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


