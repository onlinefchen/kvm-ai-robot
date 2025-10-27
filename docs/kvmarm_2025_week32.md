# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:50:54

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 310
- **总 Thread 数**: 29
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 28 threads (225 邮件)
- **RFC**: 1 threads (85 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 48 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  6 Aug 2025 12:56:22 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的一个补丁系列，主要是增加对中介虚拟性能监控单元（mediated vPMU）的支持。以下是讨论的要点：

1. **原始补丁内容**：该补丁系列（[PATCH v5 00/44]）旨在为 KVM x86 添加中介 vPMU 支持，使得虚拟机能够直接访问硬件性能监控计数器（PMC），而不需要通过 KVM 进行中介，从而提高性能。

2. **历史讨论要点**：之前的讨论集中在如何实现中介 vPMU 的功能，包括如何处理性能事件、如何在虚拟机和宿主机之间切换 PMU 状态等。补丁中提到的主要改进包括对 PMU 状态的管理、事件选择器的更新以及对性能监控计数器的直接访问。

3. **本周新讨论与进展**：本周的讨论主要围绕补丁的细节和测试结果。参与者对补丁的实现表示认可，并提到在 Intel Sapphire Rapids 平台上运行所有相关的 PMU 测试没有发现问题。补丁还引入了新的 API 以便在进入和退出虚拟机时加载和保存中介 PMU 的上下文。此外，补丁中还考虑了 AMD 和 Intel 平台的特定需求，确保了兼容性。

总的来说，这一系列补丁的目标是优化 KVM 的性能监控能力，通过中介 vPMU 提供更高效的硬件访问，同时确保与现有的性能监控机制兼容。

#### 📝 邮件列表

1. **[08-06 12:56]** [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-06 12:56]** [PATCH v5 01/44] perf: Skip pmu_ctx based on event_type
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-06 12:56]** [PATCH v5 02/44] perf: Add generic exclude_guest support
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-06 12:56]** [PATCH v5 03/44] perf: Move security_perf_event_free() call to __free_event()
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-06 12:56]** [PATCH v5 04/44] perf: Add APIs to create/release mediated guest vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-06 12:56]** [PATCH v5 05/44] perf: Clean up perf ctx time
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-06 12:56]** [PATCH v5 06/44] perf: Add a EVENT_GUEST flag
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[08-06 12:56]** [PATCH v5 07/44] perf: Add APIs to load/put guest mediated PMU context
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[08-06 12:56]** [PATCH v5 08/44] perf: core/x86: Register a new vector for handling
 mediated guest PMIs
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[08-06 12:56]** [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI vector
 on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[08-06 12:56]** [PATCH v5 10/44] perf/x86/core: Do not set bit width for unavailable counters
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[08-06 12:56]** [PATCH v5 11/44] perf/x86/core: Plumb mediated PMU capability from
 x86_pmu to x86_pmu_cap
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[08-06 12:56]** [PATCH v5 12/44] perf/x86/intel: Support PERF_PMU_CAP_MEDIATED_VPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[08-06 12:56]** [PATCH v5 13/44] perf/x86/amd: Support PERF_PMU_CAP_MEDIATED_VPMU for
 AMD host
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[08-06 12:56]** [PATCH v5 14/44] KVM: VMX: Setup canonical VMCS config prior to kvm_x86_vendor_init()
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[08-06 12:56]** [PATCH v5 15/44] KVM: SVM: Check pmu->version, not enable_pmu, when
 getting PMC MSRs
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[08-06 12:56]** [PATCH v5 16/44] KVM: Add a simplified wrapper for registering perf callbacks
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[08-06 12:56]** [PATCH v5 17/44] KVM: x86/pmu: Snapshot host (i.e. perf's) reported
 PMU capabilities
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[08-06 12:56]** [PATCH v5 18/44] KVM: x86/pmu: Start stubbing in mediated PMU support
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[08-06 12:56]** [PATCH v5 19/44] KVM: x86/pmu: Implement Intel mediated PMU
 requirements and constraints
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[08-06 12:56]** [PATCH v5 20/44] KVM: x86/pmu: Implement AMD mediated PMU requirements
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[08-06 12:56]** [PATCH v5 21/44] KVM: x86/pmu: Register PMI handler for mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[08-06 12:56]** [PATCH v5 22/44] KVM: x86: Rename vmx_vmentry/vmexit_ctrl() helpers
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[08-06 12:56]** [PATCH v5 23/44] KVM: x86/pmu: Move PMU_CAP_{FW_WRITES,LBR_FMT} into
 msr-index.h header
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[08-06 12:56]** [PATCH v5 24/44] KVM: x86: Rework KVM_REQ_MSR_FILTER_CHANGED into a
 generic RECALC_INTERCEPTS
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[08-06 12:56]** [PATCH v5 25/44] KVM: x86: Use KVM_REQ_RECALC_INTERCEPTS to react to
 CPUID updates
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[08-06 12:56]** [PATCH v5 26/44] KVM: VMX: Add helpers to toggle/change a bit in VMCS
 execution controls
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[08-06 12:56]** [PATCH v5 27/44] KVM: x86/pmu: Disable RDPMC interception for
 compatible mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[08-06 12:56]** [PATCH v5 28/44] KVM: x86/pmu: Load/save GLOBAL_CTRL via entry/exit
 fields for mediated PMU
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[08-06 12:56]** [PATCH v5 29/44] KVM: x86/pmu: Use BIT_ULL() instead of open coded equivalents
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[08-06 12:56]** [PATCH v5 30/44] KVM: x86/pmu: Move initialization of valid PMCs
 bitmask to common x86
   - 发件人: Sean Christopherson <seanjc@google.com>
32. **[08-06 12:56]** [PATCH v5 31/44] KVM: x86/pmu: Restrict GLOBAL_{CTRL,STATUS}, fixed
 PMCs, and PEBS to PMU v2+
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[08-06 12:56]** [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[08-06 12:56]** [PATCH v5 33/44] KVM: x86/pmu: Bypass perf checks when emulating
 mediated PMU counter accesses
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[08-06 12:56]** [PATCH v5 34/44] KVM: x86/pmu: Introduce eventsel_hw to prepare for
 pmu event filtering
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[08-06 12:56]** [PATCH v5 35/44] KVM: x86/pmu: Reprogram mediated PMU event selectors
 on event filter updates
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[08-06 12:56]** [PATCH v5 36/44] KVM: x86/pmu: Always stuff GuestOnly=1,HostOnly=0
 for mediated PMCs on AMD
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[08-06 12:56]** [PATCH v5 37/44] KVM: x86/pmu: Load/put mediated PMU context when
 entering/exiting guest
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[08-06 12:57]** [PATCH v5 38/44] KVM: x86/pmu: Disallow emulation in the fastpath if
 mediated PMCs are active
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[08-06 12:57]** [PATCH v5 39/44] KVM: x86/pmu: Handle emulated instruction for
 mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[08-06 12:57]** [PATCH v5 40/44] KVM: nVMX: Add macros to simplify nested MSR
 interception setting
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[08-06 12:57]** [PATCH v5 41/44] KVM: nVMX: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[08-06 12:57]** [PATCH v5 42/44] KVM: nSVM: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
44. **[08-06 12:57]** [PATCH v5 43/44] KVM: x86/pmu: Expose enable_mediated_pmu parameter
 to user space
   - 发件人: Sean Christopherson <seanjc@google.com>
45. **[08-06 12:57]** [PATCH v5 44/44] KVM: x86/pmu: Elide WRMSRs when loading guest PMCs
 if values already match
   - 发件人: Sean Christopherson <seanjc@google.com>
46. **[08-08 15:30]** Re: [PATCH v5 07/44] perf: Add APIs to load/put guest mediated PMU
 context
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
47. **[08-08 16:28]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
48. **[08-08 16:35]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>

---

### Thread 2: [PATCH 00/11] support SCTLR2_ELx

**📧 邮件数**: 19 | **👥 参与者**: 4 | **📅 开始时间**: Mon,  4 Aug 2025 13:17:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 Linux 内核中 SCTLR2_ELx 寄存器的支持，涉及一系列补丁（共11个），旨在为 ARMv8.8/ARMv9.3 及以后的架构版本提供支持。

**原始补丁/问题内容**：
Yeoreum Yun 提出了一个补丁系列，主要是为 SCTLR2_ELx 寄存器引入初步支持。该寄存器的修改在当前版本的 Linux 中并不是严格必要的，但未来的架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要配置这些寄存器中的控制位。

**之前讨论要点**：
在之前的讨论中，参与者提到补丁需要引用相关规范的修订版本，以便于未来的更新。此外，KVM 相关的补丁在当前版本中可能存在冗余，建议在新版本发布后进行重基。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括对 SCTLR2_EL2 寄存器的定义、使 SCTLR2_EL1 可访问、在启动时初始化 SCTLR2_ELx 寄存器等。参与者 Mark Brown 和 Marc Zyngier 对补丁的某些部分进行了审核和反馈，指出需要更清晰地描述寄存器位的功能以及避免将功能位简单标记为 RES0。Yeoreum Yun 表示将根据反馈进行修改和重基。整体上，补丁系列在逐步推进中，但仍需解决一些构建错误和冗余问题。

#### 📝 邮件列表

1. **[08-04 13:17]** [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-04 13:17]** [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-04 13:17]** [PATCH 02/11] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[08-04 13:17]** [PATCH 03/11] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[08-04 13:17]** [PATCH 04/11] arm64: cpufeature: add FEAT_SCTLR2 feature
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[08-04 13:17]** [PATCH 05/11] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[08-04 13:17]** [PATCH 06/11] arm64: init SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[08-04 13:17]** [PATCH 07/11] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[08-04 13:17]** [PATCH 08/11] KVM: arm64: initialise SCTLR2_EL1 at __kvm_host_psci_cpu_entry()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[08-04 13:17]** [PATCH 09/11] KVM: arm64: support SCTLR2_EL1 for guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[08-04 13:17]** [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
12. **[08-04 13:17]** [PATCH 11/11] KVM: arm64: expose FEAT_SCTLR2 feature to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[08-04 13:24]** Re: [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[08-04 13:37]** Re: [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-04 14:04]** Re: [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[08-04 14:05]** Re: [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
17. **[08-04 14:11]** Re: [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[08-04 16:03]** Re: [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
19. **[08-05 17:01]** Re: [PATCH 07/11] arm64: make the per-task SCTLR2_EL1
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 3: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 16 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 10:57:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁系列（PATCH kvmtool v3 0/6）。该补丁系列的主要目标是为 kvmtool 提供对 ARMv8.3 架构中嵌套虚拟化的支持，允许用户通过命令行选项 `--nested` 启动虚拟机，并引入了一些新特性，如维护 IRQ 设置、计数器偏移控制和 FEAT_E2H0 支持等。

在历史讨论中，补丁的背景和目的被详细阐述。补丁 1 更新了内核头文件，补丁 2 实现了初步的嵌套虚拟化支持，补丁 3 增加了维护 IRQ 的设置，补丁 4 引入了计数器偏移控制，补丁 5 添加了 FEAT_E2H0 支持，补丁 6 则生成 HYP 定时器中断说明符。

在本周的新讨论中，参与者 Alexandru Elisei 提出了对补丁内容的多项建议，包括命令行选项名称的清晰性、错误信息的修改、代码中的命名规范以及对某些功能的检查是否必要等。Marc Zyngier 对这些建议进行了回应，表明对某些内容的看法，并强调了当前实现的合规性和合理性。

总体来看，本周的讨论集中在对补丁细节的审查和优化建议上，推动了嵌套虚拟化支持的进一步完善。

#### 📝 邮件列表

1. **[07-29 10:57]** [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[07-29 10:57]** [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[07-29 10:57]** [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[07-29 10:57]** [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[07-29 10:57]** [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[07-29 10:57]** [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[08-04 15:41]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[08-04 15:43]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[08-04 15:45]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[08-04 15:45]** Re: [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[08-04 15:47]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt
 specifiers
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[08-04 18:45]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-04 18:51]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[08-04 18:57]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-04 19:11]** Re: [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[08-04 19:15]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 08 Aug 2025 12:22:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE 特性的补丁集（[PATCH v6 00/12]），主要涉及三项新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。

**原始补丁内容**：
补丁集的目标是支持这三项新特性，具体包括对系统寄存器的修改、性能工具的更新以及文档的补充。补丁分为多个部分，涉及到系统寄存器的新增字段、性能事件属性的扩展等。

**之前讨论要点**：
在历史讨论中，补丁经历了多次版本迭代，主要集中在解决与其他更改的冲突、更新提交信息以及优化代码结构等方面。补丁的每个版本都在逐步完善特性支持和文档说明。

**本周新讨论及进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. 新增的 `config4` 字段用于支持数据源过滤。
2. 对新特性的测试结果显示，所有新特性均按预期工作，得到了参与者的认可。
3. 文档更新，详细描述了新特性和过滤器的使用方法。

总的来说，本周的讨论表明补丁集在功能实现上取得了显著进展，并得到了相关人员的测试和确认。

#### 📝 邮件列表

1. **[08-08 12:22]** [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[08-08 12:22]** [PATCH v6 01/12] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[08-08 12:22]** [PATCH v6 02/12] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[08-08 12:23]** [PATCH v6 03/12] perf: arm_spe: Expose event filter
   - 发件人: James Clark <james.clark@linaro.org>
5. **[08-08 12:23]** [PATCH v6 04/12] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
6. **[08-08 12:23]** [PATCH v6 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
7. **[08-08 12:23]** [PATCH v6 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
8. **[08-08 12:23]** [PATCH v6 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
9. **[08-08 12:23]** [PATCH v6 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
10. **[08-08 12:23]** [PATCH v6 09/12] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
11. **[08-08 12:23]** [PATCH v6 10/12] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
12. **[08-08 12:23]** [PATCH v6 11/12] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
13. **[08-08 12:23]** [PATCH v6 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>
14. **[08-08 13:37]** Re: [PATCH v6 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: Leo Yan <leo.yan@arm.com>
15. **[08-08 13:39]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 5: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  5 Aug 2025 14:56:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理受限寄存器的修复补丁，主要集中在保护虚拟机（pKVM）的相关问题。

1. **原始补丁内容**：该补丁系列包含四个部分，旨在修复 pKVM 中遇到的与受限寄存器访问和注入未定义异常相关的问题。补丁包括处理 AIDR_EL1 和 REVIDR_EL1 寄存器、使 vcpu_read/write_sys_reg 函数可用于 HYP 代码、在注入未定义异常时同步受保护客户机的 VBAR_EL1，以及修复 hVHE 模式下的来宾字节序检查。

2. **之前讨论要点**：本周的讨论中，参与者对补丁的具体实现进行了反馈，特别是对补丁 2 和 3 提出了细节上的建议。Will Deacon 提出了一些关于代码复杂性和内联函数大小的疑问，并要求在补丁中添加他的报告信息。

3. **本周的新讨论与进展**：Fuad Tabba 对 Will 的反馈做出了回应，并表示将根据建议进行修改。特别是在补丁 2 中，Fuad 发现了一些不必要的代码，计划在下次更新时进行修正。此外，讨论中还涉及了 vcpu_write_sys_reg 函数的有效性问题，Marc Zyngier 指出该函数在当前上下文中可能没有必要，Fuad 同意这一点并计划在后续版本中删除相关补丁。

总体而言，本周的讨论集中在对补丁的细节审查和优化建议上，参与者积极互动，推动了补丁的改进。

#### 📝 邮件列表

1. **[08-05 14:56]** [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-05 14:56]** [PATCH v1 1/4] KVM: arm64: Handle AIDR_EL1 and REVIDR_EL1 in host for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-05 14:56]** [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg available
 to HYP code
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-05 14:56]** [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on injecting
 an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-05 14:56]** [PATCH v1 4/4] arm64: vgic-v2: Fix guest endianness check in hVHE mode
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[08-05 15:35]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Will Deacon <will@kernel.org>
7. **[08-05 15:38]** Re: [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg
 available to HYP code
   - 发件人: Will Deacon <will@kernel.org>
8. **[08-05 15:39]** Re: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted
 registers for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
9. **[08-05 16:20]** Re: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted
 registers for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[08-05 16:25]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[08-05 16:51]** Re: [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg
 available to HYP code
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[08-05 19:41]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on injecting an undef exception
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-05 19:43]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 6: [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 17:52:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 arm64 SMMUv3 驱动的补丁（PATCH v3 00/29），主要目的是为 pKVM 提供 DMA 隔离支持。该补丁系列的主要改动包括直接应用于上游内核，去除了对 pKVM 的树外依赖，并增加了通过身份映射 SMMU S2 的最小 DMA 隔离支持。

在历史讨论中，参与者们对补丁的结构和内容进行了深入探讨。Jason Gunthorpe 提出了将新的 IOMMU 驱动拆分为独立补丁的建议，以便于审查和管理。同时，他对补丁中的一些术语和 API 设计提出了疑问，认为需要保持清晰和一致性。

在本周的新讨论中，Mostafa Saleh 和 Jason Gunthorpe 继续探讨如何优化补丁的设计。Mostafa 表示愿意去掉不必要的 hypercalls 和 IOMMU ops，以简化实现，并提到在未来的版本中可能会将 pKVM 驱动与现有的 ARM_SMMU_V3 驱动合并，以减少重复代码和复杂性。双方对如何处理 SMMU 访问的 MMIO 进行了讨论，认为在实现嵌套支持时，保持单一驱动管理 SMMU 会更为高效。

总体来看，本周的讨论集中在如何优化补丁结构和简化实现上，参与者们达成了一致，未来可能会推出更简洁的补丁版本。

#### 📝 邮件列表

1. **[07-28 17:52]** [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-28 17:53]** [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-30 11:42]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
4. **[07-30 15:07]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[07-30 13:47]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
6. **[07-31 14:17]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[07-31 13:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
8. **[07-31 17:44]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[08-01 15:59]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
10. **[08-04 14:41]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[08-05 14:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
12. **[08-06 14:10]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 7: [PATCH v2 0/5] KVM: arm64: FEAT_RASv1p1 support and RAS selection

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  6 Aug 2025 17:56:10 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 RASv1p1（Reliability, Availability, and Serviceability）支持的补丁系列（PATCH v2 0/5）。该补丁旨在填补 KVM 在处理 RAS 相关功能时的不足，特别是对 RASv1p1 寄存器的支持。

在历史讨论中，Marc Zyngier 提出了补丁的初步版本，主要包括对 RASv1p1 寄存器的处理和能力的添加。补丁的关键内容包括：添加表示 FEAT_RASv1p1 的能力、处理 RASv1p1 寄存器、忽略由 L1 客户机设置的 HCR_EL2.FIEN、以规范方式向客户机暴露 FEAT_RASv1p1，以及使 ID_AA64PFR0_EL1.RAS 可写。

在本周的新讨论中，参与者对补丁进行了审查和讨论。Joey Gouly 对处理 RASv1p1 寄存器的补丁表示认可，并提出了对规范方式暴露 FEAT_RASv1p1 的担忧，认为可能在新旧内核之间迁移虚拟机时会出现问题。Oliver Upton 建议考虑将 RAS_frac 设为可写，以解决潜在的迁移问题。Marc Zyngier 也意识到需要重新评估 RAS_frac 的处理方式，以确保兼容性。

总体而言，本周的讨论集中在对补丁的细节审查和潜在问题的探讨上，参与者们对如何在不同版本之间迁移 RASv1p1 表达了关注。

#### 📝 邮件列表

1. **[08-06 17:56]** [PATCH v2 0/5] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-06 17:56]** [PATCH v2 1/5] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[08-06 17:56]** [PATCH v2 2/5] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-06 17:56]** [PATCH v2 3/5] KVM: arm64: Ignore HCR_EL2.FIEN set by L1 guest's EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[08-06 17:56]** [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-06 17:56]** [PATCH v2 5/5] KVM: arm64: Make ID_AA64PFR0_EL1.RAS writable
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-07 12:12]** Re: [PATCH v2 2/5] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[08-07 13:55]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical
 manner
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[08-08 15:48]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical
 manner
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[08-09 21:19]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[08-09 21:21]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 24 Jul 2025 23:51:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）相关的两个补丁，主要集中在 ARM64 架构下的二级页表的销毁过程。

1. **原始补丁内容**：
   - 第一个补丁（PATCH 0/2）提出了定期销毁二级页表的方案，以解决在突然销毁大规模虚拟机时出现的调度警告问题。第二个补丁（PATCH 1/2）则将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个更小的函数，以便在销毁过程中能够分块释放页表并适时让出 CPU。

2. **之前讨论要点**：
   - 之前的讨论中，参与者指出在处理大规模虚拟机时，销毁过程可能会导致 CPU 调度延迟，进而影响系统性能。Oliver Upton 提到保护模式也受到类似问题的影响，建议在所有流中使用 `stage2_destroy_range()` 函数。

3. **本周的新讨论与进展**：
   - 本周，Raghavendra Rao Ananta 提出在销毁过程中频繁调用 `cond_resched()` 会导致性能下降，特别是在处理小型虚拟机时，建议仅在实际解除映射时调用该函数。Oliver Upton 随后回应，认为这是 pKVM 遍历的上限问题，并分享了一些修复补丁，以保持调度逻辑的一致性。Marc Zyngier 也提出了与 Xen 相关的补丁，修复了在 KVM 下运行 Xen 时出现的一些问题。

总体来看，讨论围绕着如何优化 KVM 的页表销毁过程，以提高性能并减少调度延迟，同时也涉及到与 Xen 兼容性的问题。

#### 📝 邮件列表

1. **[07-24 23:51]** [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-24 23:51]** [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[07-24 23:51]** [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-29 09:01]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-07 11:58]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[08-08 11:56]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[08-08 11:57]** Re: [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[08-09 15:48]** [PATCH 0/2] KVM: arm64: AT + SR accessor fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-09 15:48]** [PATCH 1/2] KVM: arm64: nv: Fix ATS12 handling of single-stage translation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[08-09 15:48]** [PATCH 2/2] KVM: arm64: Fix vcpu_{read,write}_sys_reg() accessors
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v1 0/2] KVM: arm: nv: fix AT S* behaviour

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 6 Aug 2025 14:17:54 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM 架构下的两个补丁，旨在修复 AT S12*/AT S1* 模拟中的行为问题。

**原始补丁/问题内容**：
补丁主要解决了在嵌套虚拟化环境中，AT S12*/AT S1* 指令返回 IPA（中间物理地址）而不考虑嵌套 hypervisor 的请求的问题。这一问题在 VHE（Virtualization Host Extensions）嵌套 hypervisor 中偶然得以正常工作，但在非 VHE 的情况下则会导致错误。

**之前讨论要点**：
在历史讨论中，开发者指出了此问题的复杂性，尤其是在尝试启动 DomU（用户虚拟机）时，发现 IPA 和 PA（物理地址）不相等，必须进行真实的 S2 转换。补丁的第一个部分确保 nVHE hypervisor 能够获得 S2 转换，而第二个部分则确保 hypervisor 看到的是该转换的结果。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现和细节上。开发者们对补丁的逻辑进行了深入的审查和讨论，Oliver Upton 和 Marc Zyngier 提出了对补丁逻辑的建议和改进意见，特别是关于如何正确处理 S2 转换和更新 CPU 寄存器 PAR_EL1 的问题。最终，Volodymyr Babchuk 表示会根据讨论结果修改补丁，并准备提交最终版本。整体上，讨论促进了对补丁逻辑的深入理解和完善。

#### 📝 邮件列表

1. **[08-06 14:17]** [PATCH v1 0/2] KVM: arm: nv: fix AT S* behaviour
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
2. **[08-06 14:17]** [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after 'at
 s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
3. **[08-06 14:17]** [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
4. **[08-06 10:37]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-06 18:45]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-06 19:17]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-06 11:40]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[08-06 19:56]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after 'at s*'
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-06 20:00]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
10. **[08-06 20:30]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>

---

### Thread 10: [PATCH RFC v2 0/2] KVM: arm64: PMU: Use multiple host PMUs

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 06 Aug 2025 18:09:53 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 系统中使用多个主机 PMU（性能监控单元）的补丁。补丁的核心是引入 `KVM_ARM_VCPU_PMU_V3_COMPOSITION` 属性，以便在异构系统中创建一个“复合” PMU，从而解决 vCPU 迁移到不兼容的 pCPU 时计数器停止递增的问题。这一行为虽然符合架构规范，但在 Windows 客户端中可能导致崩溃。

在历史讨论中，参与者探讨了当前的解决方案，即要求 VMM（虚拟机监控器）将 vCPU 固定在共享兼容 PMU 的 pCPU 上，这在 QEMU/libvirt 中实现起来困难且限制了可用 pCPU 的选择。

本周的新讨论中，Akihiko Odaki 提出了补丁的具体实现细节，包括如何处理溢出和对新属性的测试。Oliver Upton 对补丁的复杂性表示担忧，建议将其拆分为更小的补丁，并对新引入的事件数组概念提出了疑虑，认为可能会引发错误。他还建议在设计中考虑用户配置 PMU 事件过滤器的灵活性。Odaki 对此进行了回应，强调了当前设计的合理性，并讨论了未来可能的改进方向。

总体而言，本次讨论围绕如何在 KVM 中有效管理 PMU 的复合功能展开，涉及到补丁的实现、测试和设计决策等多个方面。

#### 📝 邮件列表

1. **[08-06 18:09]** [PATCH RFC v2 0/2] KVM: arm64: PMU: Use multiple host PMUs
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
2. **[08-06 18:09]** [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
3. **[08-06 18:09]** [PATCH RFC v2 2/2] KVM: arm64: selftests: Test guest PMUv3
 composition
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
4. **[08-06 10:20]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-07 03:24]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
6. **[08-06 19:03]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[08-07 23:06]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
8. **[08-08 16:08]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[08-09 15:15]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>

---

### Thread 11: [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 09 Aug 2025 02:33:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 FF-A（Firmware Framework for Arm）1.2 版本的支持，主要通过一系列补丁进行实现。

**原始 patch/问题内容**：
本次补丁集（PATCH v10 0/6）旨在支持 FF-A 1.2 规范，特别是引入新的 SEND_DIRECT2 ABI，使得寄存器 x4-x17 可用于消息负载。补丁确保主机不会使用低于已与虚拟机监控器协商的 FF-A 版本。

**之前讨论要点**：
在历史讨论中，补丁经历了多次版本更新，主要集中在兼容性问题和对 SMCCC（Secure Monitor Call Convention）1.2 的支持上。补丁的目标是简化接口，支持更多参数的传递，并处理 FF-A 1.2 中新增的可选接口。

**本周的新讨论、进展或结论**：
本周的讨论中，Per Larsen 提交了补丁的多个部分，包括：
1. 修正主机版本降级尝试的返回值，确保在协商后版本保持锁定。
2. 更新 FF-A 初始化和主机处理程序以使用 SMCCC 1.2。
3. 将 FFA_NOTIFICATION_* 接口标记为不支持，以防止其被传递到安全区。
4. 将 FF-A 1.2 接口标记为不支持，以避免被代理。
5. 在处理 FFA_FEATURE 调用时掩码响应以确保返回的最小缓冲区大小正确。
6. 将支持的 FF-A 版本提升至 1.2，以启用 1.2 特有的消息接口。

所有补丁均获得了 Will Deacon 的认可，表明讨论和补丁的方向得到了积极反馈。

#### 📝 邮件列表

1. **[08-09 02:33]** [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[08-09 02:33]** [PATCH v10 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[08-09 02:33]** [PATCH v10 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[08-09 02:33]** [PATCH v10 3/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[08-09 02:33]** [PATCH v10 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[08-09 02:33]** [PATCH v10 5/6] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[08-09 02:33]** [PATCH v10 6/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 12: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Sat,  2 Aug 2025 18:40:21 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复页表转储中可执行属性的打印问题。历史讨论中，Wei-Lin Chang 提出了补丁，指出当前的页表转储在打印可执行属性时存在反向显示的问题，即非可执行区域显示为 "X"，而可执行区域显示为空格。补丁通过交换这两个字符串来解决此问题。

在随后的讨论中，Anshuman Khandual 提出了对补丁的质疑，指出 KVM_PTE_LEAF_ATTR_HI_S2_XN 宏的语义已经是反向的，可能导致理解上的混淆。Wei-Lin Chang 进一步分析了代码逻辑，确认了当前实现的逻辑与预期不符，认为应该将 "X" 和空格的打印逻辑调整为符合实际。

本周的新讨论中，Mark Rutland 提出了一个关键问题：在掩码中包含 PTE_VALID 位可能导致不必要的复杂性，建议将其移除并单独处理。Anshuman Khandual 和 Sebastian Ene 也支持这一观点，认为应当简化过滤逻辑，以便与 Stage-1 页表转储保持一致。最终，Wei-Lin Chang 表示感谢大家的反馈，并计划根据讨论结果提交补丁的第二版。

#### 📝 邮件列表

1. **[08-02 18:40]** [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-03 19:33]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[08-04 20:41]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[08-04 16:22]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[08-05 05:10]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[08-05 08:31]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Sebastian Ene <sebastianene@google.com>
7. **[08-07 11:12]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 13: [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 13:00:05 +0100

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM（Protected KVM）相关的补丁系列，特别是关于在虚拟机初始化期间保留 pKVM VM 句柄的问题。

1. **原始补丁内容**：Fuad Tabba 提出的补丁系列（[PATCH v1 0/8]）旨在确保在虚拟机初始化时为 pKVM 分配一个唯一的 VM 句柄，以便在主机内核和虚拟机监控程序之间共享和跟踪虚拟机。

2. **之前讨论要点**：在之前的讨论中，Fuad 还提到需要重命名 `pkvm.enabled` 字段为 `pkvm.is_protected`，以消除对虚拟机状态的混淆。Wei-Lin Chang 对此表示关注，并询问未来是否会允许用户选择是否启动受保护的虚拟机。

3. **本周的新讨论与进展**：在本周的讨论中，Fuad 确认了正在将 pKVM 上游化的进程，并提到 Android 中已有的支持受保护虚拟机的代码示例。他解释了如何在创建虚拟机时设置新类型 `KVM_VM_TYPE_ARM_PROTECTED`，以标识受保护的虚拟机。Wei-Lin 对此表示感谢并确认理解，Kunwu Chan 则对补丁进行了审核并表示认可。

总体来看，本周的讨论进一步明确了 pKVM 的开发方向和具体实现细节，为未来的功能扩展奠定了基础。

#### 📝 邮件列表

1. **[07-29 13:00]** [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-29 13:00]** [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-03 14:10]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[08-04 08:00]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-04 20:20]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
6. **[08-08 19:32]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>

---

### Thread 14: [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  7 Aug 2025 13:01:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理受限寄存器的修复补丁，主要针对保护虚拟机（protected VMs）的相关问题。

**原始 patch/问题内容**：
该补丁系列旨在解决在 pKVM（用于 Android 的下游代码）中遇到的与保护虚拟机访问受限寄存器及向保护客体注入未定义异常相关的问题。补丁包括三个部分，分别处理 AIDR_EL1 和 REVIDR_EL1 的主机处理、同步保护客体的 VBAR_EL1 以及修复 hVHE 模式下的客体字节序检查。

**之前讨论要点**：
在本周之前没有相关的历史讨论，所有讨论均为本周新进展。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上。Fuad Tabba 提出了三个补丁，分别解决了上述问题。Oliver Upton 在最后一封邮件中确认已将这些补丁应用于修复分支，并感谢 Fuad 的贡献。这表明补丁得到了认可并已进入后续开发流程。

#### 📝 邮件列表

1. **[08-07 13:01]** [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-07 13:01]** [PATCH v2 1/3] KVM: arm64: Handle AIDR_EL1 and REVIDR_EL1 in host for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-07 13:01]** [PATCH v2 2/3] KVM: arm64: Sync protected guest VBAR_EL1 on injecting
 an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-07 13:01]** [PATCH v2 3/3] arm64: vgic-v2: Fix guest endianness check in hVHE mode
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-08 10:51]** Re: [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers for protected VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 15: [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 21:15:03 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 规范的补丁集（PATCH v9 0/6）。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用更多寄存器作为消息负载。补丁的主要目的是防止主机使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，因为虚拟机监控器缺乏必要的兼容性路径来进行版本转换。

在之前的讨论中，Per Larsen 提出了多个补丁，包括使用 SMCCC 1.2 进行 FF-A 初始化，并将某些 FF-A 1.2 接口标记为不支持，以避免被代理。讨论中强调了 SMCCC 1.2 的重要性，因为它支持更多的返回寄存器。

在本周的新讨论中，Will Deacon 对 Per Larsen 的补丁表示支持，并建议无条件使用 SMCCC 1.2，以确保与 SMC 代理代码的兼容性。此外，他对标记为不支持的 FF-A 1.2 接口表示认可，并提出安全侧应负责拒绝相关请求。整体来看，本周的讨论进一步确认了补丁的方向和必要性。

#### 📝 邮件列表

1. **[07-30 21:15]** [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-30 21:15]** [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-30 21:15]** [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[08-08 13:39]** Re: [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Will Deacon <will@kernel.org>
5. **[08-08 13:41]** Re: [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 16: [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 12:33:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，主要集中在移除 `vm_dead` 检查并基于 `vm_bugged` 来处理 -EIO 错误的提议。

1. **原始补丁内容**：Sean Christopherson 提出了一个补丁，建议移除 `vm_dead` 的检查，转而仅依赖 `vm_bugged` 来拒绝 ioctls。理由是 `vm_dead` 的检查存在竞争条件，可能导致错误的安全感，而 `vm_bugged` 的使用则可以有效限制由于内核或硬件错误造成的损害。

2. **之前讨论要点**：在历史讨论中，参与者们关注到移除 `vm_dead` 检查可能会导致在死虚拟机中创建和运行 vCPUs，这显然是不理想的。Adrian Hunter 提出了需要更多的检查来避免 TDX VCPU 子-IOCTL 与 `tdx_mmu_release_hkid()` 之间的竞争。

3. **本周的新讨论与进展**：在本周的讨论中，Chao Gao 表达了对补丁的支持，并建议在 `tdx_sept_remove_private_spte()` 中添加注释，以明确 `!is_hkid_assigned()` 表示客人已终止，从而可以直接回收私有页面，而无需清除。这表明对补丁的理解和支持逐渐达成一致。

总体来看，讨论围绕如何安全地处理虚拟机状态和资源管理展开，参与者们在细节上进行深入探讨，以确保补丁的有效性和安全性。

#### 📝 邮件列表

1. **[07-29 12:33]** [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 12:33]** [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-01 16:56]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>
4. **[08-01 09:44]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-06 14:06]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Chao Gao <chao.gao@intel.com>

---

### Thread 17: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  7 Aug 2025 09:21:28 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 ARM64 代码中将 `BUG_ON(1)` 替换为 `BUG()` 的补丁。Arnd Bergmann 提出了这个补丁，原因是 `BUG_ON()` 宏在某些情况下会增加复杂性，并可能导致编译器的控制流分析出现误报，特别是在使用 clang-21 时，出现了未初始化变量的警告。

在历史讨论中，虽然没有具体的邮件记录，但可以推测 Arnd 之前曾对相关的构建报告做出过回应，并意识到这个问题的存在。

在本周的新讨论中，Nathan Chancellor 对补丁进行了审核并表示支持，确认了其有效性。Oliver Upton 则表示已将该补丁应用于修复中，确认了补丁的合并。因此，这个补丁得到了社区的认可，并成功解决了相关的编译警告问题。

#### 📝 邮件列表

1. **[08-07 09:21]** [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Arnd Bergmann <arnd@kernel.org>
2. **[08-07 08:56]** Re: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Nathan Chancellor <nathan@kernel.org>
3. **[08-08 10:51]** Re: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 18: [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 14:04:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Armv8.8 SPE（可扩展性能监控）特性的补丁集。历史讨论中，James Clark 提出了一个包含 12 个补丁的补丁集，旨在支持三项新 SPE 特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤以及 SPE_FEAT_FDS 数据源过滤。这些特性可以独立应用，并且补丁集还包括了相应的系统寄存器更改和性能工具的调整。

在之前的讨论中，James 还提到了一项补丁（第 5 个补丁），旨在提取一个宏以检查 SPE 版本，以提高代码的可读性，并没有引入功能性变化。

本周的新讨论中，Leo Yan 对第 5 个补丁进行了回复，指出他在主线内核中无法应用该补丁，原因是他的本地代码树缺少一个必要的提交（ae344bcb0d49），该提交更新了 `__init_el2_fgt`，因此需要对补丁进行相应的更新。Leo 提供了具体的反馈，表明补丁的应用存在问题，并建议进行修正。

#### 📝 邮件列表

1. **[07-21 14:04]** [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[07-21 14:04]** [PATCH v5 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
3. **[08-08 10:18]** Re: [PATCH v5 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 19: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 15:54:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“启用 mmap() 用于 guest_memfd”。该补丁的主要目的是为不使用 KVM_MEMORY_ATTRIBUTE_PRIVATE 的虚拟机类型支持主机用户空间对 guest_memfd 支持的内存进行映射。

在历史讨论中，Sean Christopherson 提到 arm64 的补丁已获得 Marc 的审核，x86 部分也已准备就绪，等待 Paolo 的批准。他强调了尽快将此补丁合并到 kvm/next 的重要性，特别是因为 x86 Kconfig 的更改可能与正在进行的其他系列产生语义冲突。此外，补丁还扩展了 guest_memfd 的自测试，以全面测试主机用户空间 mmap 功能，确保 mmap 操作的成功、数据的完整性以及与 fallocate 的交互。

在本周的新讨论中，Shivank Garg 对补丁进行了审核并表示支持，确认了补丁的有效性。这表明该补丁在社区中获得了积极的反馈，进一步推动了其合并的进程。整体来看，讨论集中在补丁的审核和测试方面，显示出对 KVM 功能扩展的重视。

#### 📝 邮件列表

1. **[07-29 15:54]** [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 15:54]** [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-07 13:42]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Shivank Garg <shivankg@amd.com>

---

### Thread 20: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 16:51:36 +0100

#### 🤖 AI 总结

在本邮件线程中，Marc Zyngier 提出了一个补丁（patch），旨在为 KVM 的 UUID 添加一个独立的自测试功能，以便在 UUID 出现问题时能够及时发现。补丁的主要内容是增加一个自测试文件 `kvm-uuid.c`，用于检查 KVM 的 UUID 是否符合预期。

在之前的讨论中，Andrew Jones 提出了对补丁的建议，询问是否应该检查返回值 `res.a0` 是否等于 `SMCCC_RET_SUCCESS`。他认为这种检查方式在自测试中变得越来越常见，可能需要引入一个 ucall 辅助函数来简化这一过程。

在本周的新讨论中，Marc Zyngier 对之前的讨论进行了回应，指出 Andrew 的建议并不适用于 KVM，因为在 KVM 中，返回值 A0-A3 包含完整的 UID，而检查 A0 是否等于 SUCCESS 是无效的。他表示将删除这一无意义的断言，并感谢 Andrew 的反馈。

总体来看，此次讨论围绕 KVM UUID 的自测试功能展开，补丁的提出和后续的反馈表明了开发者对确保系统稳定性的重视。

#### 📝 邮件列表

1. **[07-21 16:51]** [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-22 11:18]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for
 KVM's own UUID
   - 发件人: Andrew Jones <ajones@ventanamicro.com>
3. **[08-06 18:10]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 20:58:41 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）处理虚拟机中的同步外部中止（SEA）的问题，主要由 Jiaqi Yan 提出。原始的补丁（PATCH v3 0/3）旨在解决当主机的 APEI（ACPI Platform Error Interface）无法处理 SEA 时，KVM 直接向虚拟 CPU 注入异步 SError 的问题，这种做法通常会导致虚拟机内核崩溃。补丁的核心是通过 KVM_EXIT_ARM_SEA 机制，使 VMM（虚拟机监控器）能够更有效地处理这种情况，尤其是在现代数据中心服务器中，虚拟 CPU 可能会遇到可恢复的未更正内存错误（UER）。

在之前的讨论中，Jiaqi Yan 指出，当前的处理方式虽然可以阻止损坏内存的传播，但在虚拟机自动重启后，可能会重新使用已损坏的内存，导致更严重的问题。

本周的讨论中，Jiaqi Yan 对补丁进行了友好的提醒，寻求对其补丁的审查。这表明该补丁仍在等待社区的反馈和进一步的评估。整体来看，讨论集中在改善 KVM 对 SEA 的处理机制，以提高虚拟化环境的稳定性和可靠性。

#### 📝 邮件列表

1. **[07-31 20:58]** [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 20:58]** [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[08-06 08:03]** Re: [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 22: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Jul 2025 11:23:42 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上处理由于 VNCR（Virtual Non-Canonical Register）重定向引起的 SEAs（Synchronous External Aborts）。历史讨论中，Oliver Upton 提出了一个补丁，旨在将重定向到 VNCR 页的系统寄存器访问也能生成外部中止，并通过 kvm_handle_guest_sea() 进行处理，以便可能的 APEI（ACPI Platform Error Interface）处理，如果内核未处理该中止，则回退到 vSError。此外，他还提到将删除一个无用的 kvm_ras.h 头文件。

在本周的新讨论中，Oliver Upton 表示该补丁已被应用于修复中，并感谢参与者的贡献。这表明该补丁得到了认可并已进入代码库，显示出讨论的积极进展。

#### 📝 邮件列表

1. **[07-29 11:23]** [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[08-08 10:51]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  6 Aug 2025 18:13:41 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试功能，具体是增加一个独立的测试用例来检查 KVM 的 UUID。Marc Zyngier 提出的补丁（patch）旨在通过自测试来检测 KVM UUID 是否被篡改，以便及早发现潜在问题。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是基于对 KVM UUID 可靠性关注的背景。Marc Zyngier 在补丁中详细描述了 UUID 的重要性，并提供了相应的代码实现，包括在 `Makefile.kvm` 中添加测试程序和创建新的测试源文件 `kvm-uuid.c`。

在本周的新讨论中，Marc Zyngier 的补丁得到了 Oliver Upton 的认可，并已被应用到修复分支中。这表明该补丁经过审查并被认为是有效的，能够增强 KVM 的稳定性和安全性。整体来看，此次讨论强调了对 KVM UUID 监测的重要性，并推动了相关测试功能的实现。

#### 📝 邮件列表

1. **[08-06 18:13]** [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-08 10:51]** Re: [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 24: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 11:18:28 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 VNCR_EL2 相关故障的补丁。历史讨论中，Marc Zyngier 提出了一个补丁，旨在修正对 ESR_EL2.VNCR 位的检查方式。他指出，原先的实现错误地检查了 ESR_EL2.DFSC 中的随机位，而不是专注于 ESR_EL2.VNCR 位的设置。这导致了在处理权限和翻译故障时未能正确识别问题。此外，他建议将 BUG_ON() 改为 WARN_ON_ONCE()，以避免在此处崩溃。

在本周的新讨论中，Oliver Upton 确认了该补丁已被应用到修复列表中，并表示感谢。这表明该补丁得到了认可并成功整合进代码库，解决了之前提到的问题。整体来看，这一讨论强调了对 KVM 在处理特定故障时的准确性和稳定性的关注。

#### 📝 邮件列表

1. **[07-30 11:18]** [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-08 10:51]** Re: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 14:07:36 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在解决 Clang 编译器发出的关于未初始化常量指针的警告。

**原始 patch/问题的内容**：Justin Stitt 提出的补丁旨在禁用 Clang 22 中出现的一个警告，具体是关于传递给 `get_clidr_el1()` 函数的 `@clidr` 变量被认为是未初始化的常量指针。由于该函数实际上并不关心常量属性，因此这个警告被认为是误报。

**之前讨论要点**：在历史讨论中，Stitt 详细描述了警告的来源及其影响，指出该警告并不影响代码的实际运行，并提出了通过禁用该警告来解决问题的建议。

**本周的新讨论、进展或结论**：在本周的讨论中，Nathan Chancellor 对该补丁表示认可，认为这是一个合适的解决方案，并给予了审核通过的反馈。这表明该补丁在社区中得到了支持，预计将会被合并到稳定版本中。

#### 📝 邮件列表

1. **[07-28 14:07]** [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning
   - 发件人: Justin Stitt <justinstitt@google.com>
2. **[08-06 15:25]** Re: [PATCH 6.1.y] KVM: arm64: sys_regs: disable
 -Wuninitialized-const-pointer warning
   - 发件人: Nathan Chancellor <nathan@kernel.org>

---

### Thread 26: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 31 Jul 2025 08:56:59 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中支持 FF-A（Firmware Framework for Arm）版本提升至 1.2 的补丁（patch）。该补丁旨在确保在支持新版本时，能够正确处理未定义的位（MBZ）并避免潜在的向后兼容性问题。

在历史讨论中，Marc Zyngier 提到，尽管当前版本更新频繁，但需要确保在支持新版本前，旧版本的 MBZ 位必须为零，以便在未来版本中能够准确理解这些位的含义。他强调，未定义的位在新版本中应当被强制执行为零。

本周的新讨论中，Will Deacon 对之前的讨论进行了总结，指出目前已经协商了一个已知的 FF-A 版本，确保不会是 v1.337，并希望规范的作者不会在后续版本中破坏已有的功能。他还提到，解析的响应来自于信任区（TZ），在调用 FFA_FEATURES 后，如果 MBZ 位非零，则应予以忽略。

总体而言，讨论集中在如何安全地提升 FF-A 的版本支持，并确保向后兼容性和正确处理未定义位的问题。

#### 📝 邮件列表

1. **[07-31 08:56]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-05 15:49]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 27: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 10 Aug 2025 21:12:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Clang 堆栈深度跟踪的补丁系列（PATCH v3 00/13），该补丁已被应用于 riscv/linux.git 代码库中。

补丁的主要内容包括：
1. 将 `STACKLEAK` 重命名为 `KSTACK_ERASE`，以更好地反映其功能。
2. 将 `stackleak_track_stack` 重命名为 `__sanitizer_cov_stack_depth`，以增强可读性。
3. 处理不同架构（如 x86、arm、arm64、s390、powerpc、mips）中 KCOV 的初始化与内联不匹配问题。
4. 支持 Clang 堆栈深度跟踪的功能实现。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出该补丁系列的开发背景与目的在于提升内核的安全性和可维护性，尤其是在堆栈跟踪和错误检测方面。

本周的新进展是补丁系列已成功应用，并得到了 Kees Cook 的确认。邮件中列出了每个补丁的具体变更和相关链接，显示出开发者对代码质量和功能实现的重视。整体来看，此次补丁的应用标志着对内核安全性的进一步增强。

#### 📝 邮件列表

1. **[08-10 21:12]** Re: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking
   - 发件人: patchwork-bot+linux-riscv@kernel.org

---

### Thread 28: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat,  9 Aug 2025 21:53:56 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 ptdump 功能进行的补丁（PATCH v2）。该补丁的主要目的是移除 PTE_VALID 属性在测试中的干扰，以便更准确地显示内存页表的属性。

在历史讨论中并没有相关的上下文，邮件中只包含了本周的讨论内容。Wei-Lin Chang 提出了该补丁，指出在 stage-2 的 ptdump 中，PTE_VALID 被错误地包含在 R、W、X 和 AF 属性的测试中，这导致了可执行属性输出的混淆。为了解决这个问题，补丁移除了所有属性掩码和测试值中的 PTE_VALID，使每个测试仅匹配相关的位。此外，补丁还更新了可执行属性的打印格式，使其与 stage-1 ptdump 一致，非可执行区域打印为 "NX"，可执行区域打印为 "x "。

本周的讨论中，补丁经过测试并得到了建议者的认可，修改了属性输出格式，并提供了与之前版本的链接。整体来看，该补丁旨在提高 KVM 在 arm64 架构下的内存页表属性显示的准确性和一致性。

#### 📝 邮件列表

1. **[08-09 21:53]** [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v1 00/38] ARM CCA Device Assignment support

**📧 邮件数**: 85 | **👥 参与者**: 10 | **📅 开始时间**: Mon, 28 Jul 2025 19:21:37 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM CCA（可信计算架构）设备分配支持的 RFC 补丁系列，主要由 Aneesh Kumar K.V 提出。该补丁系列旨在实现 ARM CCA 架构下的设备分配功能，基于 Alp12 规范进行代码更改，并扩展了 TSM（可信安全管理）框架，以支持主机和客户机的设备分配工作流。

在历史讨论中，参与者们对补丁的具体实现进行了深入探讨，涉及 DMA 分配、设备通信支持、设备状态管理等多个方面。Jason Gunthorpe 提出了对某些补丁的疑虑，特别是关于 iommufd 的设计选择和 DMA 地址生成的规则。

在本周的新讨论中，参与者们继续对补丁进行审查和反馈。Aneesh 对 Jonathan Cameron 的建议表示感谢，并承诺将根据反馈更新补丁。此外，讨论中还涉及了如何处理设备状态、DMA 映射的有效性以及如何确保在不同情况下的内存管理和安全性。

总体而言，讨论集中在如何优化补丁以确保 ARM CCA 设备分配的安全性和有效性，同时解决参与者提出的技术细节问题。

#### 📝 邮件列表

1. **[07-28 19:21]** [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[07-28 19:21]** [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[07-28 19:21]** [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private memory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[07-28 19:21]** [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[07-28 19:21]** [RFC PATCH v1 06/38] iommufd: Add and option to request for bar mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[07-28 19:21]** [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[07-28 19:21]** [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[07-28 19:21]** [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[07-28 19:21]** [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[07-28 19:21]** [RFC PATCH v1 14/38] coco: host: arm64: Device communication support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[07-28 19:21]** [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the physical device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[07-28 19:21]** [RFC PATCH v1 18/38] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[07-28 19:21]** [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[07-28 19:21]** [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual device communication
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
15. **[07-28 19:22]** [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
16. **[07-28 19:22]** [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest initiated TDI bind/unbind
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
17. **[07-28 19:22]** [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range found in the interface report
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
18. **[07-28 19:22]** [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start and stop support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
19. **[07-28 19:22]** [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create parameters
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
20. **[07-28 19:22]** [RFC PATCH v1 37/38] coco: guest: arm64: Add support for fetching device measurements
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
21. **[07-28 19:22]** [RFC PATCH v1 38/38] coco: guest: arm64: Add support for fetching device info
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
22. **[07-28 11:08]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
23. **[07-28 11:17]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
24. **[07-28 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
25. **[07-29 13:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
26. **[07-29 13:58]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
27. **[07-29 11:29]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
28. **[07-29 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
29. **[07-30 14:55]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
30. **[07-30 14:52]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
31. **[07-30 14:57]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
32. **[07-30 15:08]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
33. **[07-30 15:13]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
34. **[07-30 15:26]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
35. **[07-31 11:36]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
36. **[07-31 14:39]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
37. **[07-31 09:22]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
38. **[07-31 19:07]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
39. **[08-01 12:51]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
40. **[08-01 14:19]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
41. **[08-02 14:14]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
42. **[08-02 10:41]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
43. **[08-04 08:02]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
44. **[08-04 09:47]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
45. **[08-04 09:52]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
46. **[08-04 09:59]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
47. **[08-04 10:15]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
48. **[08-04 10:20]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
49. **[08-04 12:07]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
50. **[08-04 12:18]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
51. **[08-04 12:28]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
52. **[08-04 11:27]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
53. **[08-04 13:58]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
54. **[08-04 11:23]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
55. **[08-04 16:52]** Re: [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
56. **[08-04 16:54]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
57. **[08-04 17:00]** Re: [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
58. **[08-04 17:03]** Re: [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
59. **[08-04 17:25]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
60. **[08-04 17:26]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
61. **[08-04 17:27]** Re: [RFC PATCH v1 37/38] coco: guest: arm64: Add support for
 fetching device measurements
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
62. **[08-04 17:27]** Re: [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start
 and stop support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
63. **[08-04 17:27]** Re: [RFC PATCH v1 18/38] X.509: Move certificate length retrieval
 into new helper
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
64. **[08-04 17:28]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
65. **[08-04 17:28]** Re: [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
66. **[08-04 17:29]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
67. **[08-04 17:31]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
68. **[08-04 17:31]** Re: [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create
 parameters
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
69. **[08-05 11:29]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
70. **[08-05 10:26]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
71. **[08-05 10:20]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
72. **[08-05 10:37]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
73. **[08-05 14:54]** Re: [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
74. **[08-05 20:22]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
75. **[08-05 12:48]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
76. **[08-05 12:54]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
77. **[08-05 13:08]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
78. **[08-05 13:10]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
79. **[08-05 14:27]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
80. **[08-05 11:27]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
81. **[08-05 15:42]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
82. **[08-05 12:06]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
83. **[08-05 16:38]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
84. **[08-06 14:18]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
85. **[08-08 23:37]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Eric Biggers <ebiggers@kernel.org>

---

